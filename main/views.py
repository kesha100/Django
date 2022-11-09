from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import datetime
from .models import Film, Director
from .forms import CreateDirectorForm, CreateFilmForm, UserCreateForm, UserLoginForm


def search_view(request):
    search_word = request.GET.get('search_word')
    context = {
        'search_word': search_word,
        'films': Film.objects.filter(title__icontains=search_word)
    }
    return render(request, 'search.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/films/')
            else:
                return redirect('/login/')
    return render(request, 'login.html', context)


def register_view(request):
    context = {
        'form': UserCreateForm()
    }
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/')
        context['form'] = form
    return render(request, 'register.html', context)


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


PAGE_SIZE = 3


def films_list_view(request):
    page = int(request.GET.get('page', 1))
    all_films = Film.objects.all()
    film_list = all_films[(page - 1) * PAGE_SIZE: page * PAGE_SIZE]
    total = all_films.count()
    pages_amount = total // PAGE_SIZE if total % PAGE_SIZE == 0 else total // PAGE_SIZE + 1
    films_list = {
        'films_list': film_list,
        'buttons': [i for i in range(1, pages_amount + 1)],
        'previous': page - 1,
        'next': page + 1,
        'page': page,
        'pages_amount': pages_amount
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


