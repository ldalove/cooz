# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccs', '0003_auto_20160909_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='univcounselingcenter',
            name='webSite',
            field=models.URLField(blank=True),
        ),
    ]
