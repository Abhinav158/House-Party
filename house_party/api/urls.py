# Store all URLs local to this particular app 

from django.urls import path
from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view())
]