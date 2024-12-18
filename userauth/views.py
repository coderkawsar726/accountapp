from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
# Create your views here.

def AuthView(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('main:menu')
		else:
			messages.error(request,"Invalid username or password")
	else:
		username = ""
		password = ""
	return render(request, 'index.html', {'username':username, 'password':password})


def Dashboard(request):
	return render(request, 'dashboard.html', {})


class SignUp(CreateView):
	model = User
	fields = ['first_name', 'last_name', 'email', 'username', 'password']

	template_name = 'signup.html'
	success_url = reverse_lazy('auth:login')

def UserLogout(request):
	logout(request)
	return redirect('auth:login')
