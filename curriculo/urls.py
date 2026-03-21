from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('get/<int:pk>/', views.get, name='get'),
    path('get-list/', views.get, name='getList'),
    path('search/', views.search, name='search'),

]