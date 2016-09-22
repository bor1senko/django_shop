# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20160907_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='booleanproperty',
            name='parent',
            field=models.ForeignKey(default=1, to='task.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stringproperty',
            name='parent',
            field=models.ForeignKey(default=1, to='task.Product'),
            preserve_default=False,
        ),
    ]
