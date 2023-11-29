from django.shortcuts import render
from ipmclients.forms import AddClientForm
from ipmalpha.models import *
from ipmalpha.forms import *
from ipmclients.models import *

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

