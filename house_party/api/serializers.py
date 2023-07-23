'''
A serializer takes a model with python code and translates the python code 
into a JSON Response by representing them in key-value pairs
'''

from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')