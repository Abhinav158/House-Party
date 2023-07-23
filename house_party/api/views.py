# This is where we write our endpoint rendering 
from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Write an API View which views a list of all the different Rooms
class RoomView(generics.ListAPIView):
    queryset         = Room.objects.all()
    serializer_class = RoomSerializer


