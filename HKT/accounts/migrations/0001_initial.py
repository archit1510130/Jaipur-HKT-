# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-12 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField(blank=True, default=0)),
                ('fullname', models.CharField(default='', max_length=100)),
            ],
        ),
    ]