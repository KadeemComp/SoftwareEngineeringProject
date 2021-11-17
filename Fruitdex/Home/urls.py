from  django.urls import path
from . import views

#The "" means no additional arguments

app_name = 'Home'
urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name="greet"),
    path('login', views.greet, name='login')
]