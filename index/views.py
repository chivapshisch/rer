from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import generics 
from .models import * 
from .serializers import * 
from django.http import Http404

class Ehai(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = AllInf

class Vybor(APIView):
    def get_queryst(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        snip = self.get_queryst(pk)
        serializer = CarsSerializer(snip)
        return Response(serializer.data)

class NewCar(generics.CreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class Change(APIView):
    def try_putter(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404
    
    def put(self, request, pk):
        snip = self.try_putter(pk)

   
        ser = CarsSerializer(snip)
        data = {
            'town': ser.data['town'],
            'number': ser.data['number'],
            'model': ser.data['model'],
            'price': request.data['price'],
            'status': request.data['status'],
            'cvet': ser.data['cvet'],
            'god_vypuska': ser.data['god_vypuska']
        }
        serial_end = CarsSerializer(data = data)
        if serial_end.is_valid():
            serial_end.save()
            return Response(serial_end.data)