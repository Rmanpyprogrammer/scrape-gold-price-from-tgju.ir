from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView ,
    ListAPIView,

    RetrieveAPIView,
    DestroyAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import *
from rest_framework.views import APIView
from rest_framework.decorators import  api_view,permission_classes
from rest_framework.response import Response


@api_view(["POST"])
def Price_online_get(request):
    Data=request.data
    Price_online.objects.create(
        value=Data,
        date=datetime.now()
    )
    return Response({
        "message":"ok"},
         status=status.HTTP_201_CREATED    
    )
