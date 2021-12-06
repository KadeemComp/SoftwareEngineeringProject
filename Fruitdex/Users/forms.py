from django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile

#Changing the feilds belows changes the info required on sign up
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
<<<<<<< Updated upstream
        fields = ['username', 'email','password1','password2']
=======
        fields = ['username', 'email', 'password1','password2']
>>>>>>> Stashed changes


#This form is for undating the user's account information
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
<<<<<<< Updated upstream
        fields = ['username', 'email']
=======
        fields = ['username', 'email',]
>>>>>>> Stashed changes


#This form is for undating the user's profile
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']