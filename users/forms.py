from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields='__all__'
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Your Full Name'
                }),
                'slug': forms.TextInput(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Slug'
                }),
                'bio': forms.TextInput(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Bio'
                }),
                'dob': forms.DateInput(attrs={
                    'type': 'date',
                    'class': "date_input",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Date of Birth'
                }),
        }