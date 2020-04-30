from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('formularz/', views.formularz, name='blog-formularz'),
]