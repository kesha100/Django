from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index_view(request):
    return HttpResponse('<h1>Welcome<h1/>')


def about_us(request):
    return render(request , 'about_us.html')


def date_now(request):
        """Shows today's current time and date."""
        today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        context = {'today': today}
        return render(request, 'date_now.html', context)


