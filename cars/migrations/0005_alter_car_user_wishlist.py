# Generated by Django 4.1.7 on 2023-03-23 05:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0004_car_user_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user_wishlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='Wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]