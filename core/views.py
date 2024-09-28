from django.shortcuts import render
from django.http import request


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')



def contacts(request):
    return render(request, 'contacts.html')


def recipes(request):
    return render(request, 'recipes.html')


def register(request):
    return render(request, 'register.html')
