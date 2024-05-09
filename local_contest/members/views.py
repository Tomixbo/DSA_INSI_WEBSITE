from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from challenges.utils import update_ranks


def login_user(request):
    if request.user.is_authenticated:
        update_ranks()
        return redirect('challenge_list')
    else:
        if request.method == "POST":
            username = request.POST["username"].lower()
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, (f"You were logged as : {username.capitalize()}"))
                return redirect('challenge_list')
                
            else:
                messages.success(request, ("Error : verify username/password, and try again..."))
                return redirect('login')
        else:
            return render(request, 'authenticate/login.html', {})

def logout_user(request):
    messages.success(request, ("You were logged out!"))
    logout(request)
    return redirect('login')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('challenge_list')
    else:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username'].lower()
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("Registration successfull!"))
                return redirect('challenge_list')

        else:
            form = RegisterUserForm()

        return render(request, 'authenticate/register_user.html', {'form':form,})
