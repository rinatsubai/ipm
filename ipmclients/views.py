from typing import Any
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
    return render(request, 'clients.html', {'clients': Client.objects.all(), 'clientform': clientform, 'all_projects': all_projects,})


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
        