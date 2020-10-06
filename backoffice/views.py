from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'dashboard.html')

def deposit(request):
	return render(request, 'deposit.html')
