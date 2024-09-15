from django.shortcuts import render
from chat.models import Room


def main_view(request):
    context = {
        'rooms': Room.objects.all()
    }
    return render(request, 'main/main.html', context)
