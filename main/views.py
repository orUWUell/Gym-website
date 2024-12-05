from django.shortcuts import render
from django.views.generic import ListView

from chat.models import Room, Genre
from .forms import GenreForm


def main_view(request):
    get = request.GET
    if get.get('q'):
        rooms = Room.objects.filter(name__icontains=get['q'])
    elif get:
        rooms = Room.objects.filter(genres__name__in=get).distinct()
    else:
        rooms = Room.objects.all()
    genre_form = GenreForm()
    context = {
        'rooms': rooms,
        'form': genre_form,
    }

    return render(request, 'main/main.html', context)



class SearchView(ListView):

    template_name = 'main/main.html'
    context_object_name = 'rooms'
    paginate_by = 5

    def get_queryset(self):
        return Room.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context