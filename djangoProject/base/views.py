from django.http import HttpResponse
from django.shortcuts import render

from base.models import Room


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
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         roam = i
    context = {'roam': roam}
    return render(request, 'base/Room.html', context)
