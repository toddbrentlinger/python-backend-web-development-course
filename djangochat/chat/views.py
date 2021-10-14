from django.shortcuts import render, redirect
from .models import Room

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if not Room.objects.filter(name=room).exists():
        new_room = Room.objects.create(name=room)
        new_room.save()

    return redirect('/'+room+'/?username='+username)