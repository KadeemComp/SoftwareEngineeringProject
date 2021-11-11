from django.shortcuts import render, resolve_url
from django.http import HttpResponse, response

# Create your views here.
def index(request):
    return render(request, "Users/index.html" )