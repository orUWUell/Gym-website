from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Room, Message
from .forms import RoomForm
from django.views.generic import DetailView
# Create your views here.


@login_required(login_url='login')
def chat_view(request, pk):
    room = get_object_or_404(Room, id=pk)
    messages = Message.objects.filter(room=room)
    context = {
         'room': room,
         'messages': messages,
    }
    return render(request, 'chat/lobby.html', context)


@login_required
def create_room(request):
    errors = False
    if request.method == 'POST':
        room = Room(
            name=request.POST['name'],
            question=request.POST['question'],
            creator=request.user
        )
        room.save()
        return redirect(reverse_lazy("homepage"))
    form = RoomForm()
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'chat/create_room.html', context)
