"""
URL configuration for ipm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ipmalpha.views import main_page, second_page
from ipmclients.views import clients_page, clients_filter
from ipmfinance.views import finance_page
from ipmalpha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_page, name="main_page"),
    path('finance/', finance_page, name="finance_page"),
    path('clients/', clients_page, name="clients_page"),
    path('filter/', clients_filter, name="clients_filter"),
    path('client/<slug:client_slug>', clients_filter, name="clients_filter"),
    path('', views.ProjectListView.as_view(), name="second"),
    path('api/', views.ProjectListAPIView.as_view()),
    
]
