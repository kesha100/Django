from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import datetime
from .models import Film, Director
from .forms import CreateDirectorForm, CreateFilmForm


def create_director_view(request):
    print(request.POST)
    context = {
        'form': CreateDirectorForm
    }
    if request.method == 'POST':
        form = CreateDirectorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/directors/')

    return render(request, 'create_director.html', context=context)


def create_film_view(request):
    context = {
        'form': CreateFilmForm()
    }
    if request.method == 'POST':
        form = CreateFilmForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')

    return render(request, 'create_film.html', context=context)


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
    return render(request, 'film_detail.html', context=dict_)


def directors_view(request):
    directors_list = {
        'directors': Director.objects.all()
    }
    return render(request, 'directors.html', context=directors_list)


def director_films_view(request, director_id):
    dict_ = {}
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        raise Http404('Director not found :(')
    dict_['director'] = director
    dict_['directors'] = Director.objects.all()
    return render(request, 'director_detail.html', context=dict_)

