# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-13 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0003_auto_20160913_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='html',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='email',
            name='text',
            field=models.TextField(blank=True, default=b''),
        ),
    ]