# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0019_auto_20160914_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyname',
            old_name='parent',
            new_name='product',
        ),
    ]
