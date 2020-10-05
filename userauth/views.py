from django.shortcuts import render,redirect
from .forms import CreateForm
# Create your views here.
def UserRegisterView(request):
	form = CreateForm()
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request, 'practice.html', context)

def another(request):
	return render(request, 'hello.html')


