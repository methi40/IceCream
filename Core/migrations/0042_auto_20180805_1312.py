# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-08-05 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0041_blog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]