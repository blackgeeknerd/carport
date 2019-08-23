# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-08-23 12:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20190823_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False, help_text='Designates whether the user is a vershified user', verbose_name='user verified'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, verbose_name='sex'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Driver', 'Driver'), ('Passenger', 'Passenger')], max_length=30, verbose_name='user type'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, default='user.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
