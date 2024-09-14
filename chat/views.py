from django.http import HttpResponse
from django.shortcuts import render
from .models import Message
from django.views import View
# Create your views here.


class IndexView(View):
    def post(self, request):
        if request.method == "POST":
            text = request.POST['text']
            new_message = Message(text=text)
            new_message.save()

    def get(self, request):
        if request.method == "GET":
            messages = Message.objects.all()
            context = {'messages': messages}
            return render(request, 'chat/lobby.html', context)

