from django.db import models


class Comments(models.Model):
    "База комментариев пользователей"
    name = models.CharField(max_length = 50, verbose_name="Имя пользователя")
    comment = models.TextField(max_length=200, verbose_name="Комментарий")

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
        verbose_name = "Запись"
        verbose_name_plural="Записи"


class Products(models.Model):
    "База продуктов для продажи"
    title = models.CharField(max_length=150, verbose_name="Продукт")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='products/photos/', blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


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

        