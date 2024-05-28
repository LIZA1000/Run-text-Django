from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .utils import create_runtext_video
import os


def home(request):
    text = request.GET.get('text', default='')
    if text:
        filename = "scrolling_text.mp4"
        create_runtext_video(text, filename)
        response = FileResponse(open(filename, 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename="scrolling_text.mp4"'
        return response
    else:
        return HttpResponse("Please provide text parameter, e.g., ?text=Hello")
