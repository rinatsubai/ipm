from django.contrib import admin
from django.urls import include, path
from ipmclients.views import clients_filter, ClientAPIView, clients_new_page, clients
from ipmalpha import views
from ipmalpha.views import projects_page
from rest_framework.routers import SimpleRouter, DefaultRouter
from dashboard.views import dashboard 

router = DefaultRouter()
router.register(r'api/clients', ClientAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name="dashboard"),
    path('clients/', clients, name="clients"),
    path('filter/', clients_filter, name="clients_filter"),
    # path('client/<slug:client_slug>', clients_filter, name="clients_filter"),
    # path('', views.ProjectListView.as_view(), name="main_page"),
    path('projects/', projects_page, name="projects_page"),
    # path('projects/', new_projects_page.as_view(), name="new_projects_page"),
    path('api/', views.ProjectListAPIView.as_view()),
    path('', include(router.urls)),
    path('', include("ipmclients.urls")),
    path('', include("ipmalpha.urls")),
    path('', include("finance.urls")),
]
