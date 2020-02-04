from django.urls import include, path
from rest_framework import routers
from .views import register

urlpatterns = [
   ##path('register'),
   path('register/',register)
]