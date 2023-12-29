from django.urls import path
from ipmclients import views
from .views import *

urlpatterns = [
    path("clients/<slug:pk>", ClientDetailView.as_view(), name="client_view"),
    path("clients/<slug:client_id>/update/", client_update, name="client_update"),
    path("clients/<slug:client_id>/delete/", client_delete, name="client_delete"),
    
]