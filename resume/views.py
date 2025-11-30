from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

def index(request):
    return render(request, 'resume/index.html')

def resume(request):
    return render(request, 'resume/resume.html')