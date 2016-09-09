# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CounselCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('telno', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('imported_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]