from django.forms import *

from chat.models import Genre


class GenreForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(GenreForm, self).__init__(*args, **kwargs)
        genres = Genre.objects.values_list('name', flat=True)
        for genre in genres:
            self.fields[f'{genre}'] = BooleanField(label=genre, required=False)