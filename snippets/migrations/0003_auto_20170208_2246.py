# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20170208_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ('created', 'title')},
        ),
    ]
