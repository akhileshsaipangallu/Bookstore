# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20170315_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bank',
            new_name='publisher',
        ),
    ]