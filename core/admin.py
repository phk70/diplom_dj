from django.contrib import admin

from .models import Comments, Posts, Products, Recipies, Users

# Простая регистрация
# admin.site.register(Comments)
# admin.site.register(Posts)
# admin.site.register(Products)
# admin.site.register(Users)

# Регистрация моделей через классы с редактированием отображения модели для пользователя


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'published_date']


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'context']
    list_filter = ['published_date']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo', 'price']
    list_filter = ['title']
    search_fields = ['title']
    # prepopulated_fields = {"slug": ("title", )}


@admin.register(Recipies)
class RecipiesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo']
    list_filter = ['title']
    search_fields = ['title']
    # prepopulated_fields = {"slug": ("title", )}


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'telephone']
    list_filter = ['name']    