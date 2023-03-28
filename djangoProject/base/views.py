from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import RoomForm

from base.models import Room, Topic


# # Create your views here.
# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Lets learn java!'},
#     {'id': 3, 'name': 'Lets learn javascript!'}
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    roam = Room.objects.get(id=pk)

    topic = Topic.objects.all()
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         roam = i
    context = {'roam': roam, 'topic': topic}
    return render(request, 'base/Room.html', context)


def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        # request.POST.get('name')
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    roam = Room.objects.get(id=pk)
    form = RoomForm(instance=roam)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=roam)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
