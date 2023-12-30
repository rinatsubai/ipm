from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    noform = True
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("error loging"))
            return redirect('login')
    else:    
        return render(request, 'main/login.html', {'noform': noform})


def logout_user(request):
    logout(request)
    return redirect('login_user')

