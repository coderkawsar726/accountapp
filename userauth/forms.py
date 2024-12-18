from django import forms
from django.contrib.auth.models import User

class UserSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}))
	class Meta:
		
		model = User 
		fields = ['first_name', 'last_name', 'email', 'username', 'password']
