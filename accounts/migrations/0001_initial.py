# Generated by Django 3.2.5 on 2021-12-08 09:08

import accounts.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('f_name', models.CharField(default='First Name', max_length=50)),
                ('l_name', models.CharField(default='Last Name', max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(blank=True, max_length=256, null=True)),
                ('profile_image', models.ImageField(blank=True, default=accounts.models.default_profile_picture_upload_location, max_length=255, null=True, upload_to=accounts.models.profile_picture_upload_location)),
                ('cover_image', models.ImageField(blank=True, default=accounts.models.default_cover_picture_upload_location, max_length=255, null=True, upload_to=accounts.models.profile_cover_upload_location)),
                ('privacy', models.CharField(choices=[('1', 'Private'), ('2', 'Public')], default='1', max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('otp', models.CharField(blank=True, max_length=9, null=True)),
                ('count', models.IntegerField(default=0, help_text='Number of OTP Sent')),
                ('validated', models.BooleanField(default=False, help_text='If it is true that means user have validated OTP correctly in second API')),
                ('otp_session_id', models.CharField(default='', max_length=120, null=True)),
                ('username', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
        ),
    ]
