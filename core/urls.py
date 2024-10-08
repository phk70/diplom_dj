from django.urls import path

from .views import home, about, contacts, recipes, register, shop, product_detail, add_product, update_product, delete_product

app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('register/', register, name='register'),   
    path('shop/', shop, name='shop'),    
    path('recipes/', recipes, name='recipes'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('update-product/<int:id>/', update_product, name='update_product'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
]