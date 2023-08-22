from django.urls import path
from .views import Homework

urlpatterns = [
    path('', Homework)
]