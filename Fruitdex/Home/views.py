import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.files.storage import default_storage  # provides lazy access to the current default storage system 
from django.contrib import messages # used to add a message call
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from Users.models import Profile
from .models import Fruit

#here we have a response to a request which renders an HTML page
def index(request):
    return render(request, "Home/index.html")

def logo(request):
    return render(request, "Home/index.html")


def browse(request):
    content = {
        'fruits': Fruit.objects.all() #If this is changed, change "context_object_name" as well
    }
    return render(request,"Home/browse.html", content)

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        fruits = Fruit.objects.filter(fruit_name__contains=searched)
        return render(request,"Home/search_fruit.html", {'searched': searched, 'fruits':fruits})
    else:
        return render(request,"Home/search_fruit.html", )

class FruitListView(ListView):
    model = Fruit
    template_name = 'Home/browse.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'fruits' #This is the variable passed into the browse page. It will need to be changed
    ordering = ['fruit_name'] #attribute from database


class FruitDetailView(DetailView):
    model = Fruit
    

class FruitCreateView(LoginRequiredMixin ,CreateView):
    model = Fruit
    fields = ['image','fruit_name','content']

    profile = Profile

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.request.user.profile.contribution += 1
        self.request.user.save()
        return super().form_valid(form)


class FruitUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Fruit
    fields = ['image','fruit_name','content']

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
