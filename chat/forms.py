from .models import Room
from django import forms


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'question', 'genres']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form_name',
                'placeholder': 'Название вашей комнаты',
            }),
            'question': forms.Textarea(attrs={
                'class': 'form_question',
                'placeholder': 'Введите свой вопрос'
            }),
            'genres': forms.CheckboxSelectMultiple({
                'class': 'form_genres_checkboxes',
            })
        }
