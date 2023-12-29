from django.urls import path
from ipmclients import views
from .views import *

urlpatterns = [
    path("clients/<slug:pk>", ClientDetailView.as_view(), name="client_view"),
    path("clients/old/<slug:pk>", ClientDetailView.as_view(), name="client_detail"),
    path("clients/<slug:client_id>/update/", client_update, name="client_update"),
    path("clients/<slug:client_id>/delete/", client_delete, name="client_delete"),
    # path('api/clients', views.ClientAPIView.as_view()),
    path("clients-2", clients_new_page, name="clients_new_page"),
]