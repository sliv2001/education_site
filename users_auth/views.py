"""
The module contains views, which implement processing and HTML generation.
"""
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from geo_site.views import index
from .forms import UserRegisterForm

def register(request):
    """
    View for user registration page
    """
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
    """
    View for user signout (no page, redirect only).
    """
    auth.logout(request)
    return redirect(index)
