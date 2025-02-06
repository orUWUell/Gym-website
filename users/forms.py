
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super(UserRegistrationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #
    #     return user

#
# class UserUpdateForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'profile_picture', 'description']
#         widgets = {
#             'description': forms.Textarea(attrs={'class': 'description',
#                                                  'placeholder': 'Description',}),

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'description', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username',}),
            'description': forms.Textarea(attrs={'class': 'description'}),
            'profile_picture': forms.FileInput(attrs={'class': 'avatar-uplod'
                                                      }),

        }

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class CustomChangePasswordForm(PasswordChangeForm):
    class Meta:
        my_default_errors = {
            'required': 'This d is required',
            'old_password': 'Enter a valid value'
        }
        model = get_user_model()
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'password', 'id': 'current-password'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'password', 'id': 'new-password'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'password', 'id': 'confirm-new-password'}),
        }
