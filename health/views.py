from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

#simple 200 ok response for health check requests

class HealthView(APIView):
    allowed_methods = ['GET']
    
    def get(self, request):
        return Response(status=status.HTTP_200_OK)