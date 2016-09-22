# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_propertyname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booleanproperty',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='stringproperty',
            name='parent',
        ),
        migrations.AlterField(
            model_name='booleanproperty',
            name='key',
            field=models.ForeignKey(to='task.Property'),
        ),
        migrations.AlterField(
            model_name='stringproperty',
            name='key',
            field=models.ForeignKey(to='task.Property'),
        ),
    ]
