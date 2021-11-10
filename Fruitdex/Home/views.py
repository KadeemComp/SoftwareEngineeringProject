from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#here we have a responce to a request which renders an HTML page
def index(request):
    return render(request, "Home/index.html")


#The following are test views

def kadeem(request):
    return HttpResponse("Good day to you!")

def song(request):
    return HttpResponse("Hello, Song!")


#takes a custom string and added it to the HttpResponse
#in this case it should place the text at the end of the URL into the HTML file

def greet(request, name):
    return render(request, "Home/greet.html", {
        "name": name
    })
