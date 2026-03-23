from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo/', views.create, name='novo'),
    path('criar/', views.create, name='criar'),
    path('curriculo/<int:pk>/', views.get, name='curriculo'),
    path('pesquisar/', views.search, name='pesquisar'),

]