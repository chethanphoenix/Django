# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.FileField(blank=True, upload_to=b'', verbose_name='Article_image'),
        ),
    ]
