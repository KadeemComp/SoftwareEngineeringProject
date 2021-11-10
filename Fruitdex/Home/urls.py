from  django.urls import path
from . import views

#The "" means no additional arguments

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name="greet"),
    path("kadeem", views.kadeem, name="kadeem"),
    path("song", views.song, name="song")
]