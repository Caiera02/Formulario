from django.contrib import admin
from django.urls import path,include
from formulario.views import avaliacao_view,teste_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/',teste_view, name='pagina_de_sucesso'),
    path('avaliacao/', avaliacao_view, name='new_avaliacao'),
]
