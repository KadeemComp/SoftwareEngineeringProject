from  django.urls import path
from .views import (
    FruitListView, 
    FruitDetailView, 
    FruitCreateView,
    FruitUpdateView,
    FruitUpdateNameView,
    FruitDeleteView,
)
from . import views

#set up Upload image url

#The "" means no additional arguments which makes it the default page
urlpatterns = [
    path('', views.index, name = 'index'),
    path('browse', FruitListView.as_view(), name='browse'),
    path('fruit/<int:pk>/', FruitDetailView.as_view(), name='fruit-detail'),
    path('fruit/new/', FruitCreateView.as_view(), name='fruit-create'),
    path('fruit/<int:pk>/update/', FruitUpdateView.as_view(), name='fruit-update'),
    path('fruit/<int:pk>/delete/', FruitDeleteView.as_view(), name='delete'),
    path('fruit/<int:pk>/update_name/', FruitUpdateNameView.as_view(), name='update-name'),
    # path('fruit/<int:pk>/Add_local_name/', FruitAddLocalNameView.as_view(), name='add-local-name'),
    path('search', views.search, name='search-fruit'),
]