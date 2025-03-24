from django.urls import path
from .views import avaliacao_view

urlpatterns = [
    path('avaliacao/', avaliacao_view, name='avaliacao'),
]