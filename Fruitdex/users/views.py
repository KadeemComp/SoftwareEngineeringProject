from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import  messages
from Home import views as home_views
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, "Users/index.html" )

def login_view(request):
    return render(request, "Users/login.html" )

def  logout_view(request):
    pass

def signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(home_views.index)
    else:
        messages.error(request, f'Username or password is invalid' )
        form = UserRegistrationForm()
    return render(request, "Users/signup.html" , {'form': form})
