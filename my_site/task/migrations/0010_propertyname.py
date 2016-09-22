# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_booleanproperty_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(to='task.Property')),
            ],
        ),
    ]
