# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_auto_20160907_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.ForeignKey(default=1, to='task.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='product',
            field=models.ForeignKey(to='task.Product'),
        ),
    ]
