# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150207_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('time',)},
        ),
    ]
