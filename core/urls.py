from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from core.views import home, about, contacts, recipes, register, shop

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('register/', register, name='register'),   
    path('shop/', shop, name='shop'),    
    path('recipes/', recipes, name='recipes'),    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)