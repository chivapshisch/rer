from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import generics 
from .models import * 
from .serializers import * 

class Ehai(APIView):
    def get(self, request):
        snip = Cars.objects.all()
        serializer = CarsSerializer(snip, many = True)
        return Response(serializer.data)

    def post(self, requset):
        serializer = CarsSerializer(data = requset.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        else:
            error = ({'error': error})
            return Response(error)