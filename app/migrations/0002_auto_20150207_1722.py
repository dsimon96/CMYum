# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restaurant', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('time', models.DateTimeField(verbose_name=b'time placed')),
                ('user_location', models.CharField(max_length=50)),
                ('runner', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('hashedPassword', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('firstName',),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='app.User'),
            preserve_default=True,
        ),
    ]
