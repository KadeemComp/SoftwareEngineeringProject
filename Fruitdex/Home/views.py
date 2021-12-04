from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pyrebase
from .models import Fruits
#dummy data of fruits

fruits = [
    {
       'name':'mango',
       'scientific_name': 'something',
       'content': {'Grenada - mango', 'Trinidad - mango'},
       'author': 'jane doe',
       'date_posted': 'December 2nd, 2018'
    },
    {
       'name':'apple',
       'scientific_name': 'somethingElse',
       'content': {'Grenada - apple', 'Trinidad - apple'},
       'author': 'john Doe',
       'date_posted': 'December 1st, 2018'
    },
    {
       'name':'apple',
       'scientific_name': 'somethingElse',
       'content': {'Grenada - apple', 'Trinidad - apple'},
       'author': 'john Doe',
       'date_posted': 'December 1st, 2018'
    },
     {
       'name':'apple',
       'scientific_name': 'somethingElse',
       'content': {'Grenada - apple', 'Trinidad - apple'},
       'author': 'john Doe',
       'date_posted': 'December 1st, 2018'
    }
    ]


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


@login_required
def addfruit(request):
    return render(request,"Home/addfruit.html")


def browse(request):
    content = {
        'fruits': fruits,
        #'fruits_from_database': Fruits.objects.all()
    }
    return render(request,"Home/browse.html", content)