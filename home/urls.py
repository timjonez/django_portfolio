from django.urls import path
from .views import ProjectView, resume_view

urlpatterns = [
    path('', ProjectView.as_view(), name='project_list'),
    path('resume/', resume_view),
]