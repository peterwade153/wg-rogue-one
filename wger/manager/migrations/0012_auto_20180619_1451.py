# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-19 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_workout_exported_from'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='exported_from',
            new_name='imported_from',
        ),
    ]
