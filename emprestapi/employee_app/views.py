
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee

from rest_framework import status

# Create your views here.
class EmployeeAPI(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "status" : "success",
            data : {
                "name" : "rachit",
                "class" : 12,
                "rollnumber" : 15,
                "address": "kanpur",
            }
        }
        return response(data=data)

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            return response({"status": "success", "data" : serializer.data},status=status.HTTP_200_OK)

        else:
            return response({"status": "error occured", "data": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
