from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy

class CreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1','password2']




