from django.contrib import admin
from django.urls import include, path
from ipmclients.views import clients_page, clients_filter, ClientSerialAPI
from ipmalpha import views
from ipmalpha.views import projects_page
from rest_framework.routers import SimpleRouter, DefaultRouter
from dashboard.views import dashboard 

router = DefaultRouter()
router.register(r'api/clients', ClientSerialAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name="dashboard"),
    path('clients/', clients_page, name="clients_page"),
    path('filter/', clients_filter, name="clients_filter"),
    # path('client/<slug:client_slug>', clients_filter, name="clients_filter"),
    # path('', views.ProjectListView.as_view(), name="main_page"),
    path('projects/', projects_page, name="projects_page"),
    path('api/', views.ProjectListAPIView.as_view()),
    path('', include(router.urls)),
    path('', include("ipmclients.urls")),
    path('', include("ipmalpha.urls")),
]
