import time
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ipmclients.forms import AddClientForm
from ipmalpha.models import *
from ipmalpha.forms import *
from finance.models import *
from ipmclients.models import *
from ipmalpha.filters import *
from django.views.generic import ListView, DetailView
from ipmalpha.serializers import ProjectSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# PROJECTS PAGE

def projects_page(request):
    all_projects = Project.objects.all()    
    successmessagetext = ""
    if request.method == 'POST':
        projectform = AddProjectForm(request.POST)
        if projectform.is_valid():
            successmessagetext = 'Successfully created the project'
            try:
                projectform.save()
                messages.success(request, 'Project Added')
                return HttpResponseRedirect(reverse('projects_page'))    
            except:
                projectform.add_error(None, "Error")
                projectform = AddProjectForm()
    else:
        projectform = AddProjectForm()
    client_results = Client.objects.all()
    return render(request, 'projects_page.html', {'projects': Project.objects.all(), 'projectform': projectform, 'all_projects': all_projects, 'transaction': Transaction.objects.all(), 'showclient': client_results, 'successmessagetext': successmessagetext})


# LIST API VIEW

class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProjectFilter


# LIST VIEW

class ProjectListView(ListView):
    queryset = Project.objects.all()
    template_name = 'projects_page.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProjectFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_status_color(self):
        projectslist = Project.object.all()
        for p in projectslist:
            pstatus = p.project_status
            p_status_color = pstatus.status_color
        return p_status_color.value
    pass
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['projecsall'] = Project.objects.all()

        return context
    
def projects_page_2(request):
    return render(request, 'projects-2.html')