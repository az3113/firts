# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='acceso',
            new_name='accesoPaypal',
        ),
    ]
