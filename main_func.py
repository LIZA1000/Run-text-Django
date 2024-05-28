from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpy
import numpy as np


def create_runtext_video(text, filename="my_file.mp4", duration=3, size=(100, 100), fps=30):
    width, height = size
    font_size = 80
    try:
        font = ImageFont.truetype("arialmt.ttf", font_size)
    except IOError:
        print("Ошибка: шрифт 'arialmt.ttf' не найден.")
        return

    # Длина текста в пикселях
    text_width = font.getbbox(text)[2] - font.getbbox(text)[0]

    # Количество кадров
    num_frames = duration * fps

    def make_frame(t):
        frame = Image.new("RGB", size, color=(0, 0, 0))
        draw = ImageDraw.Draw(frame)

        # Положение текста на каждом кадре
        x = int(width - text_width / num_frames * (t // (3 / num_frames)))
        y = height // 2 - font_size // 3 * 2
        draw.text((x, y), text, font=font, fill=(0, 153, 76))

        return np.array(frame)

    # Создание и сохранение видео
    clip = mpy.VideoClip(make_frame, duration=duration)
    clip = clip.set_duration(duration).set_fps(fps)
    clip.write_videofile(filename, codec="libx264")


# Пример использования
create_runtext_video("яz", "my_file.mp4")
