from django.urls import path 
from .views import *

urlpatterns = [
    path("cars/", Ehai.as_view()),
]