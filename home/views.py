from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.core.mail import send_mail, BadHeaderError

from .models import Project
from .forms import ContactForm


class ProjectView(ListView):
    model = Project
    template_name = 'home/home.html'


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject'] + ' ' + from_email
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'contact@timjones.tech', ['timjonez@protonmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header')
            return redirect('success/')
    return render(request, "home/email.html", {'form':form})


def success_view(request):
    return TemplateResponse(request, 'home/success.html', {})


def resume_view(request):
    return TemplateResponse(request, 'home/resume.html', {})
