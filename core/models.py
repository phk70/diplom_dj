from django.db import models


class Comments(models.Model):
    "База комментариев пользователей"
    name = models.CharField(max_length = 50, verbose_name="Имя пользователя")
    comment = models.TextField(max_length=200, verbose_name="Комментарий")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Posts(models.Model):
    "База постов для наполнения сайта"
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    title = models.CharField(max_length = 150, verbose_name="Заголовок")
    context = models.TextField(verbose_name="Контекст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контекст главной страницы"
        verbose_name_plural="Контекст главной страницы"


class Products(models.Model):
    "База продуктов для продажи"
    kg = 'кг'
    wt = 'шт'
    unit = (
        (kg, 'кг'),
        (wt, 'шт')        
    )

    title = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    measurement = models.CharField(max_length=2, choices=unit, default=kg)
    photo = models.ImageField(upload_to='products/photos/', blank=True, null=True, verbose_name='Фото')
    price = models.IntegerField(verbose_name="Цена")
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Recipies(models.Model):
    "База данных рецептов"
    title = models.CharField(max_length=150, verbose_name="Заголовок рецепта")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='recipies/photos/', blank=True, null=True, verbose_name='Фото')    
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

class Users(models.Model):
    "База пользователей"
    name = models.CharField(max_length=150, verbose_name="Имя пользователя")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    telephone = models.CharField(max_length=20, verbose_name='Телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        