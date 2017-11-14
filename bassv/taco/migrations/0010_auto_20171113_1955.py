# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0009_auto_20171113_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='ta',
            field=models.ManyToManyField(help_text='Select a TA for this course', to='taco.Ta'),
        ),
    ]