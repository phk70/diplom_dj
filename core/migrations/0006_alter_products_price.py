# Generated by Django 5.1.1 on 2024-10-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_comments_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Цена'),
        ),
    ]
