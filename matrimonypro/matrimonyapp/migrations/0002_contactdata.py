# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-07 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.BigIntegerField()),
                ('about', models.CharField(max_length=2000)),
            ],
        ),
    ]
