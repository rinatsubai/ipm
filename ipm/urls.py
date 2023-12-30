from django.contrib import admin
from django.urls import include, path
from ipmclients.views import clients_filter, ClientAPIView, clients
from ipmalpha import views
from ipmalpha.views import projects_page
from rest_framework.routers import SimpleRouter, DefaultRouter
from dashboard.views import dashboard, dashboardold, dashboardredirect
from users.views import login_user, logout_user

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name="dashboard"),
    path('dashboard/', dashboardredirect, name="dashboardredirect"),
    path('old/', dashboardold, name="dashboardold"),
    path('clients/', clients, name="clients"),
    path('filter/', clients_filter, name="clients_filter"),
    path('projects/', projects_page, name="projects_page"),
    path('api/', views.ProjectListAPIView.as_view()),
    path('', include("ipmclients.urls")),
    path('', include("ipmalpha.urls")),
    path('', include("finance.urls")),
    path('users/', include("django.contrib.auth.urls")),
    path('users/', include("users.urls")),
    path("signin/", login_user, name="login_user"),
    path("signout/", logout_user, name="logout_user"),
]
