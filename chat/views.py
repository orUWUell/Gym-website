from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Room, Message, Genre
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
        form = RoomForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.save()
            selected_genres = form.cleaned_data['genres']
            for genre in selected_genres:
                genre_obj = Genre.objects.get(name=str(genre))
                obj.genres.add(genre_obj)
        return redirect(reverse_lazy("homepage"))
    else:
        form = RoomForm()
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'chat/create_room.html', context)
