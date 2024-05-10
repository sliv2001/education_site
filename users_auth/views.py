from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import UserRegisterForm
from geo_site.views import index

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Создан аккаунт {username}!')
			return redirect(index)
	else:
		form = UserRegisterForm()
	return render(request, 'signup.html', context={'form': form})

def signout(request):
	auth.logout(request)
	return redirect(index)
