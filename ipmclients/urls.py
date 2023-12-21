from django.urls import path
from ipmclients import views
from .views import *

urlpatterns = [
    path("clients/<slug:pk>", ClientDetailView.as_view(), name="client_view"),
    path("clients/old/<slug:pk>", ClientDetailView.as_view(), name="client_detail"),
    # path('api/clients', views.ClientAPIView.as_view()),
    path("clients-2", clients_new_page, name="clients_new_page"),
]