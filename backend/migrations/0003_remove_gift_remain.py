# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_orderitem_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='remain',
        ),
    ]
