from django.shortcuts import render, redirect
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


def update_product(request, id):
    product = Products.objects.get(id=id)
    if request.method == "POST":
        product.title = request.POST.get("title")
        product.description = request.POST.get("description")
        product.measurement = request.POST.get("measurement")
        product.price = request.POST.get("price")
        product.photo = request.FILES.get("photo", product.photo)        
        product.save() 
        return redirect('/', permanent=True)  
    context = {
        "product": product
    }    
    return render(request, "core/update_product.html", context)


def delete_product(request, id):
    product = Products.objects.get(id=id)
    if request.method == "POST":               
        product.delete() 
        return redirect('/', permanent=True)  
    context = {
        "product": product
    }    
    return render(request, "core/delete_product.html", context)
