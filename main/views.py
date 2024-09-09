from django.shortcuts import render


def main_view(request):
    render(request, 'main/main.html')
