from django.urls import path
from . import views

app_name = 'mysqlapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questao_id>/', views.detalhes, name='detalhes'),
    path('<int:questao_id>/resultados/', views.resultados, name='resultados'),
    path('<int:questao_id>/voto/', views.voto, name='voto'),
    path('aluno/1234/', views.aluno1234, name='aluno1234'),
    path('aluno/2345/', views.aluno2345, name='aluno2345'),
    path('aluno/3456/', views.aluno3456, name='aluno3456'),
    path('ultimas5/', views.ultimas5, name='ultimas5'),
    path('participantes5/', views.participantes5, name='participantes5'),
]