# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-02-24 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_wife'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wife',
            options={'verbose_name_plural': '妻子'},
        ),
        migrations.AlterModelTable(
            name='wife',
            table='wife',
        ),
    ]