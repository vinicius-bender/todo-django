from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #rota, view responsáve, nome de referência
    path("", include("app_lista_tarefas.urls")),
    path('admin/', admin.site.urls),
]