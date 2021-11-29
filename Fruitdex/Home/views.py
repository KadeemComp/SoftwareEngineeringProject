from django.shortcuts import render
from django.http import HttpResponse
from Users.views import login_view
import pyrebase
import os


config = {
    'apiKey': "AIzaSyBzdoeJ9nOpaCctqAvDuO5u5FfnruaeHZ0",
    'authDomain': "fruitdex-imgdb.firebaseapp.com",
    'databaseURL': "https://fruitdex-imgdb-default-rtdb.firebaseio.com",
    'projectId': "fruitdex-imgdb",
    'storageBucket': "fruitdex-imgdb.appspot.com",
    'messagingSenderId': "174012390027",
    'appId': "1:174012390027:web:21fd5be54bf72a55b7928e",
    'measurementId': "G-CLPNV414GD"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()

# Create your views here.

#here we have a response to a request which renders an HTML page
def index(request):
    return render(request, "Home/index.html")


#takes a custom string and added it to the HttpResponse
#in this case it should place the text at the end of the URL into the HTML file

def greet(request, name):
    return render(request, "Home/greet.html", {
        "name": name
    })

def addfruit(request):
    return render(request,"addfruit.html")
