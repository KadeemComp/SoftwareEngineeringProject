from  django.urls import path
from . import views

#The "" means no additional arguments
#set up Upload image url

app_name = 'Home'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addfruit', views.addfruit, name='addfruit'),
    path('browse', views.browse, name='browse' ),
    #path('logo', views.logo, name='logo' )
]