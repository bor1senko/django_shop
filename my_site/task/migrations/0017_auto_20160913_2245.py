# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_prop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='prop',
            name='key',
        ),
        migrations.RemoveField(
            model_name='prop',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Man',
        ),
        migrations.DeleteModel(
            name='prop',
        ),
    ]
