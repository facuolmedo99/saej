from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Expediente
from django.contrib.auth.models import User
from django import forms

class ExpedienteForm(ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email','password1','password2']