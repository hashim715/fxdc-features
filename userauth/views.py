from django.shortcuts import render
from .forms import CreateForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here
def UserRegisterView(request):
	form = CreateForm()
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created ' + user + '.')
			return redirect('another')
	context = {'form':form}
	return render(request, 'register.html', context)
def another(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(request, username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or Password is incorrect')
	return render(request, 'login.html')
def home(request):
	return render(request, 'home.html')


