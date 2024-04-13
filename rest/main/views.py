from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView

from .serializers import HumanSerializer, Human
from rest_framework.response import Response


class HumanAPIView(generics.ListCreateAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World! Это закрытая '}
        return Response(content)


class OpenView(APIView):
    # Доступно без аутентификации
    permission_classes = []

    def get(self, request):
        content = {'message': 'Hello, World! Это открытая '}
        return Response(content)
