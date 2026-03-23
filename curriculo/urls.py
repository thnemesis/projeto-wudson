from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo/', views.create, name='novo'),
    path('criar/', views.create, name='criar'),
    path(' resumo/', views.create, name='resumoS'),
    path('curriculo/<int:pk>/', views.get, name='curriculo'),
    path('pesquisar/', views.search, name='pesquisar'),

]