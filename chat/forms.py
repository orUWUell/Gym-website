from .models import Room
from django import forms


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'question', 'genres']
        widgets = {
            'question': forms.Textarea(),
            'genres': forms.CheckboxSelectMultiple()
        }
