from  django.urls import path
from .views import FruitListView
from . import views


#set up Upload image url


#The "" means no additional arguments which makes it the default page
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addfruit', views.addfruit, name='addfruit'),
    path('browse', FruitListView.as_view(), name='browse' ),
    #path('logo', views.logo, name='logo' )
]