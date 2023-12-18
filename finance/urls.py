from django.urls import path
from finance import views
from .views import *


urlpatterns = [
    # path("clients/<slug:pk>", ClientDetailView.as_view(), name="client_detail"),
    path('finance/', finance_page, name="finance_page"),
    path('finance/lw/', finance_lw_page, name="finance_page"),
    path('api/finance', views.TransactionListAPIView.as_view()),
    path('api/financelw', views.TransactionLastWeekAPIView.as_view()),
]