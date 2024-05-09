from django.http import HttpResponse
from django.shortcuts import render
from .models import Country, LearnRate

def index(request):
    context = {
        'total_countries': Country.objects.count(),
        'user_is_auth': request.user.is_authenticated,
        'username': request.user.username,
        'learned_countries': LearnRate.objects.filter(repetition_number__gt=0, user=request.user).count() if request.user.is_authenticated else 0,
    }
    return render(request, "index.html", context=context)
