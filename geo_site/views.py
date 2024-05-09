from django.http import HttpResponse
from django.shortcuts import render
from .models import Country

def index(request):
    total_countries = Country.objects.count()
    context = {
        'total_countries': total_countries,
        'user_is_auth': request.user.is_authenticated,
        'username': request.user.username
    }
    return render(request, "index.html", context=context)
