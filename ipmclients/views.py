from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from ipmalpha.models import *
from ipmclients.forms import *
from ipmclients.models import *
from django.views.generic import ListView, DetailView
from rest_framework.viewsets import ModelViewSet
from ipmclients.serializers import *



def clients_filter(request):
    all_projects = Project.objects.all()
    if request.method == 'POST':
        clientform = AddClientForm(request.POST)
        if clientform.is_valid():
            # print(form.cleaned_data)
            # return HttpResponseRedirect("/add")    
                try:
                    clientform.save()
                    print(clientform.cleaned_data)
                    return redirect('http://127.0.0.1:8000/clients')
                    
                except:
                    clientform.add_error(None, "Error")
    
    else:
        clientform = AddClientForm()
    return render(request, 'clients_filter.html', {'clients': Client.objects.all(), 'projects': Project.objects.all(), 'clientform': clientform, 'all_projects': all_projects,})



def clients_page(request):
    all_projects = Project.objects.all()
    
    if request.method == 'POST':
        clientform = AddClientForm(request.POST)
        if clientform.is_valid():
            # print(form.cleaned_data)
            # return HttpResponseRedirect("/add")    
                try:
                    clientform.save()
                    # print(clientform.cleaned_data)
                    return redirect('http://127.0.0.1:8000/clients')
                    
                except:
                    clientform.add_error(None, "Error")
        clientform = AddClientForm()
    else:
        clientform = AddClientForm()
    return render(request, 'clients_page.html', {'clients': Client.objects.all(), 'clientform': clientform, 'all_projects': all_projects})


def clients_app(request):
    return render(request, 'clients.filter.html',)

class ClientSerialAPI(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientDetailView(DetailView):
    model = Client
    template_name = "client_detail.html"