from rest_framework import serializers 
from .models import *

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ("town","number", "model", "price", "status","cvet", "god_vypuska")

class AllInf(serializers.ModelSerializer):
    class Meta:
        model = Cars 
        fields = "__all__"