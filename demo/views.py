from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
        serializer_class = UserSerializer
        queryset = User.objects.all()
