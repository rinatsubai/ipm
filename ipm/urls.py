from django.contrib import admin
from django.urls import include, path
from ipmclients.views import clients_filter, ClientAPIView, clients
from ipmalpha import views
from ipmalpha.views import projects_page
from rest_framework.routers import SimpleRouter, DefaultRouter
from dashboard.views import dashboard, dashboardold

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name="dashboard"),
    path('old/', dashboardold, name="dashboardold"),
    path('clients/', clients, name="clients"),
    path('filter/', clients_filter, name="clients_filter"),
    path('projects/', projects_page, name="projects_page"),
    path('api/', views.ProjectListAPIView.as_view()),
    path('', include("ipmclients.urls")),
    path('', include("ipmalpha.urls")),
    path('', include("finance.urls")),
]
