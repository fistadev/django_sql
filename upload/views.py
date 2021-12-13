from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Upload

class HomeView(ListView):
    model = Upload
    template_name = 'upload/index.html'

