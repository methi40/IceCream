# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-13 13:25
from __future__ import unicode_literals

import Core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0030_auto_20160902_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='student_number',
            field=models.CharField(max_length=8, validators=[Core.models.student_number_validator]),
        ),
    ]