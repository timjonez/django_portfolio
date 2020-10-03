from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Project


class ProjectView(ListView):
    model = Project
    template_name = 'home/home.html'
