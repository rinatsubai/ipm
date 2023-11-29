from django.shortcuts import render

# Create your views here.
def finance_page(request):
    return render(request, 'finance_page.html', {})