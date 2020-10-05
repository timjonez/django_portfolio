from django.urls import path
from .views import ProjectView, resume_view, contact_view, success_view

urlpatterns = [
    path('', ProjectView.as_view(), name='project_list'),
    path('resume/', resume_view),
    path('contact/', contact_view),
    path('contact/success/', success_view),
]