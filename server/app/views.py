from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestModel
from .serializers import TestModelSerializer
# from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#API views
class TestModelEndpoints(APIView):
    def get(self, request):
        querySet = TestModel.objects.all()
        serializer = TestModelSerializer(querySet, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TestModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)