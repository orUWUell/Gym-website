from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Message
from .forms import RoomForm
from django.views.generic import DetailView
# Create your views here.


def chat_view(request, pk):
    room = get_object_or_404(Room, id=pk)
    messages = Message.objects.filter(room=room)
    context = {
         'room': room,
         'messages': messages,
    }
    return render(request, 'chat/lobby.html', context)


def create_room(request):
    errors = False
    if request.method == 'POST':
        room = Room(
            name=request.POST['name'],
            question=request.POST['question'],
            creator=request.user
        )
        room.save()
        return redirect('chat_view', pk=room.id)
    form = RoomForm()
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'chat/create_room.html', context)
