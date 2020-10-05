from django.shortcuts import render
from .forms import CreateForm
from django.shortcuts import redirect
from django.contrib import messages
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
	return render(request, 'practice.html', context)
def another(request):
	return render(request, 'hello.html')


