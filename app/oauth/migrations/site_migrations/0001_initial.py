# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-21 17:43
from __future__ import unicode_literals

import django.contrib.sites.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True, validators=[django.contrib.sites.models._simple_domain_name_validator], verbose_name='domain name')),
                ('name', models.CharField(max_length=50, verbose_name='display name')),
            ],
            options={
                'verbose_name': 'site',
                'verbose_name_plural': 'sites',
                'db_table': 'django_site',
                'ordering': ('domain',),
            },
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
    ]
