from  django.urls import path
from . import views

#The "" means no additional arguments

urlpatterns = [
    path("", views.index, name = "index")
]