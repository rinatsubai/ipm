from django.shortcuts import redirect, render
from django.db.models import Q
from ipmalpha.models import *
from ipmalpha.forms import *
from finance.models import *
from ipmclients.models import *
from ipmalpha.filters import *
from django.views.generic import ListView, DetailView
from ipmalpha.serializers import ProjectSerializer
from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.contrib import messages

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
    search_result = request.GET.get('search')
    if search_result:
        all_projects = all_projects.filter(Q(project_name__icontains=search_result)| Q(id__icontains=search_result)| Q(project_product__icontains=search_result) | Q(project_client__client_name__icontains=search_result))
    return render(request, 'projects_page.html', {'projects': all_projects, 'projectform': projectform, 'transaction': Transaction.objects.all(), 'showclient': client_results, 'successmessagetext': successmessagetext, 'projectfilterform': projectfilterform, 'search_result': search_result})

# def project_update(request, project_id):
#     project = Project.objects.get(pk=project_id)
#     projectform = AddProjectForm(request.POST, instance=project)
#     if request.method == 'POST':
#         if projectform.is_valid():
#             projectform.save()
#             return redirect('project_view')
#     return render(request, 'project_update_view.html', {'project': project, 'projectform': projectform})

def project_update(request, project_id): 
    instance = get_object_or_404(Project, pk=project_id)
    form = EditProjectForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('project_view', pk=project_id)
    return render(request, 'project_update_view.html', {'form': form}) 

def project_delete(request, project_id): 
    project = get_object_or_404(Project, pk=project_id)
    context = {'project': project}    
    if request.method == 'POST':
        project.delete()
        return redirect('projects_page')

# LIST API VIEW

class ProjectListAPIView(ListCreateAPIView):
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