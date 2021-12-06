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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from .models import Fruit
=======
import os
from .models import Fruits
#dummy data of fruits

fruits = [
    {
       'name':'mango',
       'scientific_name': 'something',
       'content': ['Grenada - mango', 'Trinidad - mango'],
       'author': 'jane doe',
       'date_posted': 'December 2nd, 2018'
    },
    {
       'name':'apple',
       'scientific_name': 'somethingElse',
       'content': ['Grenada - apple', 'Trinidad - apple'],
       'author': 'john Doe',
       'date_posted': 'December 21st, 2018'
    },
    {
       'name':'apple',
       'scientific_name': 'somethingElse',
       'content': ['Grenada - apple1', 'Trinidad - apple1'],
       'author': 'john1 Doe1',
       'date_posted': 'December 31st, 2018'
    },
     {
       'name':'apple',
       'scientific_name': 'somethingElse',
       'content': ['Grenada - apple3', 'Trinidad - apple4'],
       'author': 'John Bob Doe',
       'date_posted': 'December 5th, 2018'
    }
    ]
>>>>>>> Stashed changes
=======
from .models import Fruit
>>>>>>> Stashed changes


config = {
    'apiKey': str(os.getenv('FIREBASE_API_KEY')), # stored in environment variables for security reasons
    'authDomain': "fruitdex-imgdb.firebaseapp.com",
    'databaseURL': "https://fruitdex-imgdb-default-rtdb.firebaseio.com",
    'projectId': "fruitdex-imgdb",
    'storageBucket': "fruitdex-imgdb.appspot.com",
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()


db.child("fruit").push(fruits) # pushing the dummie data to fire



#here we have a response to a request which renders an HTML page
def index(request):
    return render(request, "Home/index.html")

def logo(request):
    return render(request, "Home/index.html")


@login_required
<<<<<<< Updated upstream
def addfruit(request):  
=======
def addfruit(request):
>>>>>>> Stashed changes
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
