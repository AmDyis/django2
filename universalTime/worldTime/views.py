from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import datetime as dt
from pytz import timezone

from .models import *

menu = ["Россия Москва", "США Нью-Йорк"]
# Create your views here.
def index(request):
    posts = TimeZone.objects.all()
    zone = dt.datetime.now(timezone("Europe/Moscow"))
    return render(request, 'TimeZone/index.html', {"menu": menu, "title": "Главное время", "posts": posts, "tz": zone.strftime("%d-%m-%Y %H:%M:%S")})

def about(request):
    return render(request, 'TimeZone/about.html', {"title": "О сайте"})

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")