# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_auto_20160914_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booleanproperty',
            old_name='parent',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='stringproperty',
            old_name='parent',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='propertyname',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
