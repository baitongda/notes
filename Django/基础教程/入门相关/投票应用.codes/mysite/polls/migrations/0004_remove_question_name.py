# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-11 01:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='name',
        ),
    ]
