# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('url', models.CharField(max_length=512)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
