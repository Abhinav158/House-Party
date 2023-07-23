from django.db import models
import string
import random

# Function to generate random unique Room Code 
def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # Make sure the generated code is unique by cross-checking with the rooms previously created in our database 
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code


# Define the fields we want to have for our room along with the constraints
class Room(models.Model):
    # Unique Room Code which users use to join in
    code            = models.CharField(max_length=8, default="", unique=True)
    # 1 user can be the host of only one room
    host            = models.CharField(max_length=50, unique=True)
    # Permission for the guest to be able to pause the music
    guest_can_pause = models.BooleanField(null=False, default=False)
    # Number of votes required to skip te current song 
    votes_to_skip   = models.IntegerField(null=False, default=1)
    # Parameter to automatically add the time of Room creation
    created_at      = models.DateTimeField(auto_now_add=True)
