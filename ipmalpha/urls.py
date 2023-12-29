from django.urls import path
from .views import *

urlpatterns = [
    path("projects/<slug:pk>", ProjectDetailView.as_view(), name="project_view"),
    path("projects/<slug:project_id>/update/", project_update, name="project_update"),
    path("projects/<slug:project_id>/delete/", project_delete, name="project_delete"),
]