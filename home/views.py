from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic.list import ListView
from .models import Project


class ProjectView(ListView):
    model = Project
    template_name = 'home/home.html'


def resume_view(request):
    return TemplateResponse(request, 'home/resume.html', {})
