from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)

class CustomTokenVerifyView(TokenVerifyView):
    permission_classes = (permissions.AllowAny,)

class HelloWorldView(APIView):
    def get(self, request):
        return Response(data={"message": "Hello, World!"}, status=status.HTTP_200_OK)
