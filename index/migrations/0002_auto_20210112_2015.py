# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-01-12 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publicate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
