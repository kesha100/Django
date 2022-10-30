from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime
from .models import Film, Director


def index_view(request):
    return render(request, 'index.html')


def about_us_view(request):
    return render(request, 'about_us.html')


def date_now_view(request):
        """Shows today's current time and date."""
        today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        context = {'today': today}
        return render(request, 'date_now.html', context)


def films_list_view(request):
    films_list = {
        'films_list': Film.objects.all(),
    }
    return render(request, 'films.html', context=films_list)


def film_detail_view(request, id):
    dict_ = {}
    try:
        film = Film.objects.get(id=id)

    except Film.DoesNotExist:
        raise Http404('Film not found :(')
    dict_['film_detail'] = film
    return render(request, 'detail.html', context=dict_)


def director_films_view(request, director_id):
    dict_ = {}
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        raise Http404('Director not found :(')
    dict_['director'] = director
    dict_['directors'] = Director.objects.all()
    return render(request, 'director.html', context=dict_)

