from urllib import response
from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework .response import Response
from .models import Quickshop
from .serializers import  QuickshopSerializer

from rest_framework import status

# Create your views here.
class QuickshopAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer =QuickshopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response({"status" : "success", "data" : serializer.data},status=status.HTTP_200_OK)

        else:
             return response({"status" : "error", "data" : serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    


