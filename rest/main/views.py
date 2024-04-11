from django.shortcuts import render
from rest_framework import generics
from .serializers import HumanSerializer, Human


class HumanAPIView(generics.ListCreateAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

