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
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

# PROJECTS PAGE

def projects_page(request):
    all_projects = Project.objects.all()    
    successmessagetext = ""
    if request.method == 'POST':
        projectform = AddProjectForm(request.POST)
        if projectform.is_valid():
            successmessagetext = 'Проект был добавлен в список проектов.'
            try:
                instance = projectform.save()
                messages.success(request, 'Добавлен проект')
                return redirect('ProjectDetailView')
                # return HttpResponseRedirect(reverse(f'projects/{instance.pk}'))
                # return redirect('clients')    
            except:
                projectform.add_error(None, "Error")
                projectform = AddProjectForm()
    else:
        projectform = AddProjectForm()
    client_results = Client.objects.all()
    projectform = AddProjectForm
    projectfilterform = FilterProjectForm
    project_name_result = request.GET.get('project_name')
    if project_name_result:
        all_projects = all_projects.filter(project_name__icontains=project_name_result)
    return render(request, 'projects_page.html', {'projects': all_projects, 'projectform': projectform, 'transaction': Transaction.objects.all(), 'showclient': client_results, 'successmessagetext': successmessagetext, 'projectfilterform': projectfilterform, 'project_name_result': project_name_result})

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
    filterset_class = ProjectFilter
    
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
    template_name = "project_view.html"
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['projecsall'] = Project.objects.all()

        return context
    
class ProjectDetailView2(DetailView):
    model = Project
    template_name = "project_detail.html"
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView2, self).get_context_data(**kwargs)
        context['projecsall'] = Project.objects.all()

        return context
    
def projects_page_2(request):
    return render(request, 'projects-2.html')