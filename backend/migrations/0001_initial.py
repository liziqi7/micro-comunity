# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('cover', models.URLField(verbose_name='\u622a\u56fe')),
                ('desc', models.TextField(verbose_name='\u4ecb\u7ecd')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('cover', models.URLField(verbose_name='\u622a\u56fe')),
                ('desc', models.TextField(verbose_name='\u4ecb\u7ecd')),
                ('remain', models.IntegerField(verbose_name='\u4f59\u91cf')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32, verbose_name='\u7528\u6237\u540d')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
                ('count', models.IntegerField(verbose_name='\u5c0f\u8ba1')),
                ('community', models.ForeignKey(to='backend.Community')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gift', models.ForeignKey(to='backend.Gift')),
                ('order', models.ForeignKey(to='backend.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('community', models.ForeignKey(to='backend.Community')),
                ('gift', models.ForeignKey(to='backend.Gift')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
