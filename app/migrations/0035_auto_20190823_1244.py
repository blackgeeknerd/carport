# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-08-23 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20190823_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Pilot', 'Pilot'), ('Passenger', 'Passenger')], max_length=30, verbose_name='user type'),
        ),
    ]
