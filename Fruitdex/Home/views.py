from django.shortcuts import render
from django.http import HttpResponse
from Users.views import login_view


# Create your views here.

#here we have a responce to a request which renders an HTML page
def index(request):
    return render(request, "Home/index.html")


def login_view(request):
    return render(request, login_view)

#takes a custom string and added it to the HttpResponse
#in this case it should place the text at the end of the URL into the HTML file

def greet(request, name):
    return render(request, "Home/greet.html", {
        "name": name
    })
