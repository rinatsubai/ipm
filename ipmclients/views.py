from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from ipmalpha.models import *
from ipmclients.forms import *
from ipmclients.models import *
from django.views.generic import ListView, DetailView
from rest_framework.viewsets import ModelViewSet
from ipmclients.serializers import *
from ipmclients.views import *
import requests
from django_filters.rest_framework import DjangoFilterBackend
from ipmclients.filters import ClientsAPIFilter
from django.contrib import messages


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



def clients(request):
    all_projects = Project.objects.all()
    all_clients = Client.objects.all()
    if request.method == 'POST':
        clientform = AddClientForm(request.POST)
        
        if clientform.is_valid():
                messages.add_message(request, messages.INFO, "Клиент был добавлен в базу.")
            # print(form.cleaned_data)
            # return HttpResponseRedirect("/add")    
                try:
                    instance = clientform.save()
                    # print(clientform.cleaned_data)
                    return redirect('clients')
                    
                except:
                    clientform.add_error(None, "Error")
                    clientform = AddClientForm()
    else:
        clientform = AddClientForm()
    clientfilterform = FilterClientForm
    search_result = request.GET.get('search')
    if search_result:
        all_clients = all_clients.filter(Q(client_name__icontains=search_result)
                                         | Q(id__icontains=search_result) 
                                         | Q(client_contact__icontains=search_result)
                                         | Q(client_telegram__icontains=search_result)
                                         | Q(client_phone__icontains=search_result)
                                         | Q(client_roletype__icontains=search_result)
                                         | Q(project__project_name__icontains=search_result))
    return render(request, 'clients.html', {'clients': all_clients, 'clientform': clientform, 'all_projects': all_projects, 'clientfilterform': clientfilterform, 'search_result': search_result})

def client_update(request, client_id): 
    instance = get_object_or_404(Client, pk=client_id)
    form = EditClientForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('client_view', pk=client_id)
    return render(request, 'client_update_view.html', {'form': form}) 

def client_delete(request, client_id): 
    client = get_object_or_404(Client, pk=client_id)
    context = {'client': client}    
    if request.method == 'POST':
        client.delete()
        return redirect('clients')

class ClientAPIView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend, )
    
class ClientDetailView(DetailView):
    model = Client
    template_name = "client_view.html"
    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['clientsall'] = Client.objects.all()

        return context
    
def clients_new_page(request):
    response = requests.get('http://127.0.0.1:8000/api/clients/')
    data = response.json
    return render(request, 'clients.html', {'data': data,})
