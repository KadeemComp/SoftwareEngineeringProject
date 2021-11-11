from django.shortcuts import render, resolve_url
from django.http import HttpResponse, response, HttpResponseRedirect
from django.urls import  reverse

# Create your views here.
def index(request):
    return render(request, "Users/index.html" )


    #if not request.user.is_authenticated():
    #   return HttpResponseRedirect(reverse("login"))


def login_view(request):
    return render(request, "Users/login.html" )

def  logout_view(request):
    pass

