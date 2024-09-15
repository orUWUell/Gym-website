from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Room, Message
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

    # def post(self, request):
    #     if request.method == "POST":
    #         text = request.POST['text']
    #         new_message = Message(text=text)
    #         new_message.save()

    # def get(self, request):
    #     if request.method == "GET":
    #
    #         return render(request, 'chat/lobby.html')

