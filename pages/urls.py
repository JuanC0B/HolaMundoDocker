# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludo, name='saludo'),  # URL para /saludo/
    path('', views.home, name='home'),  # URL para la raíz /
]
