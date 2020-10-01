from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput
from UserApp.models import UserProfile

# its for signup form


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="username", widget=forms.TextInput(
        attrs={'placeholder': 'Write Your username', }))
    email = forms.EmailField(max_length=200, label='email', widget=forms.EmailInput(
        attrs={'placeholder': 'Write Your email'}))
    first_name = forms.CharField(max_length=100, label="first_name", widget=forms.TextInput(
        attrs={'placeholder': 'Write Your first name'}))
    last_name = forms.CharField(max_length=100, label="last_name", widget=forms.TextInput(
        attrs={'placeholder': 'Write Your last name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter New Password',
                                                    'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Repeat password',
                                                    'class': 'form-control'}),
        }








   
   
  
  

   
       
    