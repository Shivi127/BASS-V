# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 02:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0004_auto_20171107_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseoffering',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='courseoffering',
            name='tid',
        ),
    ]