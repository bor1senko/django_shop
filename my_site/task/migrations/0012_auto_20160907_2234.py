# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20160907_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booleanproperty',
            name='key',
            field=models.ForeignKey(to='task.PropertyName'),
        ),
        migrations.AlterField(
            model_name='stringproperty',
            name='key',
            field=models.ForeignKey(to='task.PropertyName'),
        ),
    ]
