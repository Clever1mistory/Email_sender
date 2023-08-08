# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-08-07 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0002_auto_20230807_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a', 'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0438'},
        ),
        migrations.RenameField(
            model_name='newsletter',
            old_name='subj',
            new_name='subject',
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='sent_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
