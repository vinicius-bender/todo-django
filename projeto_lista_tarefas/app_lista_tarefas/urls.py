from django.urls import path
from . import views

urlpatterns = [
    #rota, view responsáve, nome de referência
    path('', views.home, name='home'),
    path('tarefa/<int:id>', views.tarefa, name = 'tarefa'),
    path('novatarefa/', views.novaTarefa, name='novatarefa'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('status/<int:id>', views.status, name='status'),
]