from django.urls import path
from .views import *

urlpatterns = [
    path("projects/<slug:slug>", ProjectDetailView.as_view(), name="project_detail"),
]