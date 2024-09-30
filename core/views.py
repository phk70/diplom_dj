from django.shortcuts import render
from django.http import request
from .models import Posts, Comments, Products, Recipies, Users


def home(request):
    posts = Posts.objects.all()
    comments = Comments.objects.all()
    return render(request, 'home.html', {"posts": posts, "comments": comments})


def about(request):
    return render(request, 'about.html')


def shop(request):
    products = Products.objects.all()
    return render(request, 'shop.html', {"products": products})



def contacts(request):
    return render(request, 'contacts.html')


def recipes(request):
    recipies = Recipies.objects.all()
    return render(request, 'recipes.html', {"recipies": recipies})


def register(request):
    return render(request, 'register.html')


def add_comments(request):
    pass
