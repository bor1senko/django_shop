# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_category_product_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='product',
            field=models.ForeignKey(to='task.Category'),
        ),
    ]
