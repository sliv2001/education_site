import random

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Country, LearnRate

def getCountriesNum():
    return Country.objects.count()

def index(request):
    context = {
        'total_countries': getCountriesNum(),
        'user_is_auth': request.user.is_authenticated,
        'username': request.user.username,
        'learned_countries': LearnRate.objects.filter(repetition_number__gt=0, user=request.user).count() if request.user.is_authenticated else 0,
    }

    return render(request, "index.html", context=context)

def learn(request, number):
    context = {
        'user_is_auth': request.user.is_authenticated,
        'username': request.user.username,
        'country': request.session['countries'][number][0],
        'capital': request.session['countries'][number][1],
        'region': request.session['countries'][number][2],
        'current_number': number,
        'next_number': number+1,
    }
    country_entry = Country.objects.get(name=request.session['countries'][number][0])
    try:
        entry = LearnRate.objects.get(user=request.user, country=country_entry)
    except ObjectDoesNotExist:
        entry = LearnRate.objects.create(user=request.user,
                                         country=country_entry,
                                         repetition_number=1,
                                         tests_involve=0,
                                         tests_correct=0)
    entry.repetition_number += 1
    entry.save()
        
    return render(request, "learn.html", context=context)

def getCountries(number):
    countries = []
    countriesNum = getCountriesNum()
    indexes = random.sample(range(1, countriesNum+1), number)
    for i in indexes:
        entry = Country.objects.get(id=i)
        countries.append([entry.name, entry.capital, entry.region.name])
    return countries

def learn_start(request):
    countries = getCountries(5)
    request.session['countries'] = countries
    request.session['wrong_answer']=False
    return redirect(learn, number=0)

def learn_end(request):
    request.session['wrong_answer']=False
    return redirect(index)

def learn_match(request):
    countries_capitals = request.session['countries']
    if (request.method=='POST'):
        for country, capital, region in countries_capitals:
            if request.POST.get(country, "") != capital:
                request.session['wrong_answer']=True
                return redirect(learn_match)
        messages.success(request, "Учебный тест пройден успешно!")
        request.session['practice_finished']=True
        return redirect(hoorah)
    
    # If GET request, we shuffle countries and ask user to answer
    countries = ([countries_capitals[i][0] for i in range(len(countries_capitals))])
    capitals = ([countries_capitals[i][1] for i in range(len(countries_capitals))])
    random.shuffle(capitals)
    countries_capitals = [[countries[i], capitals[i]] for i in range(len(capitals))]
    context={
        'user_is_auth': request.user.is_authenticated,
        'username': request.user.username,
        'countries': countries_capitals,
        'wrong_answer': request.session['wrong_answer']
    }
    return render(request, "learn_match.html", context=context)

def hoorah(request):
    context={
        'user_is_auth': request.user.is_authenticated,
        'username': request.user.username,
    }
    return render(request, "hoorah.html", context=context)
