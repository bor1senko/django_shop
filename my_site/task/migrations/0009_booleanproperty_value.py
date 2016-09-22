# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20160907_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='booleanproperty',
            name='value',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
