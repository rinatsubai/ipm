from django.contrib import admin
from django.urls import include, path
from ipmclients.views import clients_page, clients_filter, ClientSerialAPI
from ipmalpha import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register(r'api/clients', ClientSerialAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', clients_page, name="clients_page"),
    path('filter/', clients_filter, name="clients_filter"),
    # path('client/<slug:client_slug>', clients_filter, name="clients_filter"),
    path('', views.ProjectListView.as_view(), name="main_page"),
    path('api/', views.ProjectListAPIView.as_view()),
    path('', include(router.urls))
]
