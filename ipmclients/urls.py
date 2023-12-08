from django.urls import path
from .views import *

urlpatterns = [
    path("clients/<slug:slug>", ClientDetailView.as_view(), name="client_detail"),
]