# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0017_auto_20160913_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
        migrations.RemoveField(
            model_name='property',
            name='product',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='propertyname',
            name='type',
            field=models.CharField(default=1, max_length=100, choices=[(b'bool', b'boolean'), (b'str', b'string')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propertyname',
            name='parent',
            field=models.ForeignKey(to='task.PropertyGroup'),
        ),
        migrations.AlterField(
            model_name='stringproperty',
            name='value',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.AddField(
            model_name='propertygroup',
            name='category',
            field=models.ForeignKey(to='task.Category'),
        ),
        migrations.AddField(
            model_name='booleanproperty',
            name='group',
            field=models.ForeignKey(default=1, to='task.PropertyGroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stringproperty',
            name='group',
            field=models.ForeignKey(default=1, to='task.PropertyGroup'),
            preserve_default=False,
        ),
    ]
