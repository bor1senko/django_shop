# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_auto_20160913_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='prop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100)),
                ('key', models.ForeignKey(to='task.Car')),
                ('parent', models.ForeignKey(to='task.Man')),
            ],
        ),
    ]
