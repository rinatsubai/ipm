from django.urls import path
from .views import *

urlpatterns = [
    path("projects/<slug:pk>", ProjectDetailView.as_view(), name="project_view"),
    path("projects/old/<slug:pk>", ProjectDetailView2.as_view(), name="project_detail"),
    path('projects-2/', projects_page_2, name="projects_page_2"),
]