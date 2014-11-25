# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='number',
            field=models.IntegerField(default=1, verbose_name='\u6570\u91cf'),
            preserve_default=False,
        ),
    ]
