# Generated by Django 2.2.28 on 2023-02-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230227_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(blank=True, default='profile_images/profile1.jpg', null=True, upload_to=''),
        ),
    ]