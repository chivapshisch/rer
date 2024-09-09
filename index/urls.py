from django.urls import path 
from .views import *

urlpatterns = [
    path("cars/", Ehai.as_view()),
    path("new/", NewCar.as_view()),
    path("concret/<int:pk>/", Vybor.as_view()),
    path("change/<int:pk>/", Change.as_view()),
]