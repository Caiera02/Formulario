from django.urls import path
from .views import avaliacao_view

urlpatterns = [
    path('avaliacaoo/', avaliacao_view, name='avaliacao'),
]