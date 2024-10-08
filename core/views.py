from django.shortcuts import render, redirect
from django.http import request
from .models import Posts, Comments, Products, Recipies, Users


def home(request):
    posts = Posts.objects.all()
    comments = Comments.objects.all()
    return render(request, 'core/home.html', {"posts": posts, "comments": comments})


def about(request):
    return render(request, 'core/about.html')


def shop(request):
    products = Products.objects.all()
    return render(request, 'core/shop.html', {"products": products})


def contacts(request):
    return render(request, 'core/contacts.html')


def recipes(request):
    recipies = Recipies.objects.all()
    return render(request, 'core/recipes.html', {"recipies": recipies})


def register(request):
    return render(request, 'core/register.html')


def product_detail(request, id):
    product = Products.objects.get(id=id)
    context = {
        "product": product
    }
    return render(request, 'core/product_detail.html', context)


def add_comments(request):
    pass


def add_product(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        measurement = request.POST.get("measurement")
        price = request.POST.get("price")
        photo = request.FILES["photo"]
        product = Products(title=title, description=description, measurement=measurement, price=price, photo=photo)
        product.save() 
        return redirect('/', permanent=True)       
    return render(request, "core/add_product.html")
