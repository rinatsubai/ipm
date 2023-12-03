from django.shortcuts import render
from ipmclients.forms import AddClientForm
from ipmalpha.models import *
from ipmalpha.forms import *
from ipmclients.models import *
from ipmalpha.filters import ProjectFilter
from django.views.generic.list import ListView
from ipmalpha.serializers import ProjectSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

def second_page(request):
    project_filter = ProjectFilter(request.GET, queryset=Project.objects.all())
    context={
        'form': project_filter.form,
        'projects': project_filter.qs
    }
    return render(request, 'second.html', context)



class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProjectFilter

class ProjectListView(ListView):
    queryset = Project.objects.all()
    template_name = 'second.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProjectFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
        



    


def main_page(request):
    if request.method == 'POST':
        clientform = AddClientForm(request.POST)
        if clientform.is_valid():
            # print(form.cleaned_data)
            # return HttpResponseRedirect("/add")
            try:
                clientform.save()
                print(clientform.cleaned_data)
                # return redirect('admin')
            except:
                clientform.add_error(None, "Error")
    else:
        clientform = AddClientForm()
    context = {
            'projects': Project.objects.all()
        }
    return render(request, 'main_page.html', context)

