from django.urls import path
from .views import *

urlpatterns = [
    path("clients/<slug:pk>", ClientDetailView.as_view(), name="client_detail"),
]