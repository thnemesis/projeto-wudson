from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo/', views.novo, name='novo'),
    path('n_salvo/', views.n_salvo, name='n_salvo'),
    path('concluido/', views.concluido, name='concluido'),
    path('criar/', views.create, name='criar'),
    path(' resumo/', views.resume, name='resumo'),
    path('curriculo/<int:pk>/', views.get, name='curriculo'),
    path('pesquisar/', views.search, name='pesquisar'),
    path('salvar/', views.salvar, name='salvar'),
    path('confirmar/', views.confirmar, name='confirmar'),
    path('pdf/<int:id>/', views.gerar_pdf, name='gerar_pdf'),

]