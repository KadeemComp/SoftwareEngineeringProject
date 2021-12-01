from django.shortcuts import render
from django.http import HttpResponse
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

def logo(request):
    return render(request, "Home/index.html")

def addfruit(request):
    return render(request,"Home/addfruit.html")

def browse(request):
    return render(request,"Home/browse.html")