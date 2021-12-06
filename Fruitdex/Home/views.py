from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import pyrebase
from .models import Fruit


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
        'fruits': Fruit.objects.all() #If this is changed, change "context_object_name" as well
    }
    return render(request,"Home/browse.html", content)

class FruitListView(ListView):
    model = Fruit
    template_name = 'Home/browse.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'fruits' #This is the variable passed into the browse page. It will need to be changed
    ordering = ['fruit_name'] #attribute from database


class FruitDetailView(DetailView):
    model = Fruit
    

class FruitCreateView(LoginRequiredMixin ,CreateView):
    model = Fruit
    fields = ['fruit_name','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FruitUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Fruit
    fields = ['fruit_name','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        fruit = self.get_object()
        if self.request.user == fruit.author:
            return True
        return False


class FruitDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Fruit
    success_url = '/'

    def test_func(self):
        fruit = self.get_object()
        if self.request.user == fruit.author:
            return True
        return False
