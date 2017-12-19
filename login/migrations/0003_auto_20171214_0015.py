# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20171213_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='institute',
            field=models.CharField(choices=[('ISLT', 'Higher Institute of Languages of Tunis(ISLT)'), ('FSB', 'Faculty of Sciences of Bizerte(FSB)')], default='ISLT', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(choices=[('POE', 'Poetry'), ('SYNTAX', 'Syntax'), ('STY', 'Stylistics'), ('AMCIV', 'American Civilization'), ('LITT', 'Lit Theory')], default='LITT', max_length=120),
            preserve_default=False,
        ),
    ]
