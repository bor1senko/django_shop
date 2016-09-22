# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='p',
            field=models.ForeignKey(default=1, to='task.Product'),
            preserve_default=False,
        ),
    ]
