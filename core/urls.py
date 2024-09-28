from django.urls import path

from core.views import home, about, contacts, recipes, register, shop

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('register/', register, name='register'),   
    path('shop/', shop, name='shop'),    
    path('recipes/', recipes, name='recipes'),    
]
