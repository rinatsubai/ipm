from django.shortcuts import render
from ipmalpha.models import *
from finance.models import Transaction
from ipmclients.models import *
from django.db.models import Sum, Avg, Count, Max, Min
from django.contrib import humanize
from ipmalpha.forms import AddProjectForm, FilterProjectForm
from django.db.models import Q

from dashboard.forms import TransactionFilterForm

# Create your views here.

def dashboard(request):
    
    qs = Project.objects.all()
    sum = qs.aggregate(total=Sum("project_sum", default=0))    
    csum = qs.aggregate(Sum("transaction__amount", default=0))
    
    
    # projects form
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
    return render(request, 'dashboard.html', {'projects': all_projects, 'clients': Client.objects.all(), 'sum': sum, 'csum': csum, 'projectform': projectform, 'transaction': Transaction.objects.all(), 'showclient': client_results, 'successmessagetext': successmessagetext, 'projectfilterform': projectfilterform, 'project_name_result': project_name_result})
    
def dashboardold(request):
    qs = Project.objects.all()
    sum = qs.aggregate(total=Sum("project_sum", default=0))    
    csum = qs.aggregate(Sum("transaction__amount", default=0))
    
    return render(request, 'dashboardold.html', {'projects': Project.objects.all(), 'clients': Client.objects.all(), 'sum': sum, 'csum': csum,})

def dashboardtest(request):
    qs = Project.objects.all()
    sum = qs.aggregate(total=Sum("project_sum", default=0))    
    csum = qs.aggregate(Sum("transaction__amount", default=0))
    start_date=str(request.GET.get('transaction_date_from','1997-12-24'))
    print(start_date)
    end_date=str(request.GET.get('transaction_date_to','2099-12-24'))
    if start_date and end_date:
        transactions_filtered = Transaction.objects.filter(Q(transaction_date__gte=start_date), Q(transaction_date__lte=end_date),)
    elif start_date:
        transactions_filtered = Transaction.objects.filter(Q(transaction_date__gte=start_date),)
    elif end_date:    
        transactions_filtered = Transaction.objects.filter(Q(transaction_date__lte=end_date),)
    else:
        transactions_filtered = Transaction.objects.all()
    transactions_spendings_qs = Transaction.objects.filter(flow='OUT')
    transactions_spendings = transactions_spendings_qs.aggregate(Sum('amount', default=0))
    balance = transactions_filtered.aggregate(Sum('amount', default=0))
    transaction_filter_form = TransactionFilterForm
    return render(request, 'dashboard.html', {'projects': Project.objects.all(), 'clients': Client.objects.all(), 'sum': sum, 'csum': csum, 'transactions': transactions_filtered, 'transaction_filter_form': transaction_filter_form, 'start_date': start_date, 'end_date': end_date, 'balance': balance, 'transactions_spendings': transactions_spendings})

    










