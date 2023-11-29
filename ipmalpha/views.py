from django.shortcuts import render
from ipmclients.forms import AddClientForm
from ipmalpha.models import *
from ipmalpha.forms import *
from ipmclients.models import *
from ipmalpha.filters import ProjectFilter

def second_page(request):
    name = request.GET.get('name')
    projects_list = Project.objects.all()
    if name:
        projects_list = projects_list.filter(project_name__icontains=name)
    # project_filter = ProjectFilter(request.GET, queryset=Project.objects.all())
    context={
        'form': GetProjectsForm(), 
        'projects': projects_list
        
    }
    return render(request, 'second.html', context)

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

