# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('goodcorner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announce',
            name='hashurl',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]