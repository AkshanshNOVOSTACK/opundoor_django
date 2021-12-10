# Generated by Django 3.2.5 on 2021-12-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='address',
            field=models.CharField(max_length=30, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='community',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date joined'),
        ),
    ]