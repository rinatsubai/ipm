from django.shortcuts import render
from ipmalpha.models import *
from ipmclients.models import *
from django.db.models import Sum, Avg, Count, Max, Min
from django.contrib import humanize

# Create your views here.

def dashboard(request):
    qs = Project.objects.all()
    sum = qs.aggregate(total=Sum("project_sum", default=0))    
    csum = qs.aggregate(Sum("transaction__amount", default=0))
    print(qs)
    
    return render(request, 'dashboard.html', {'projects': Project.objects.all(), 'clients': Client.objects.all(), 'sum': sum, 'csum': csum})

    

