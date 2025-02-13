from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from serializers import UserSerializer

# Create your views here.

class UserList(generics.ListApiview):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer