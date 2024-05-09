from django.http import HttpResponse
from .models import Country
from .utils import fill_countries

def index(request):
    total_countries = Country.objects.count()
    if total_countries == 0:
        fill_countries()
    context = {
        'total_countries': total_countries,
    }
    return HttpResponse("This is the site mock.")