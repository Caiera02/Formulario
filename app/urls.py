from django.contrib import admin
from django.urls import path,include
from formulario.views import avaliacao_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('avaliacao/', avaliacao_view, name='new_avaliacao'),
]
