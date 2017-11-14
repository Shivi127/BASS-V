# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('mid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the Message', primary_key=True, serialize=False)),
                ('mstring', models.CharField(help_text='Enter the Message', max_length=200)),
            ],
        ),
    ]