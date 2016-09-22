# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_property_p'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StringProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='property',
            options={},
        ),
        migrations.RenameField(
            model_name='property',
            old_name='key',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='property',
            name='p',
        ),
        migrations.RemoveField(
            model_name='property',
            name='value',
        ),
        migrations.AddField(
            model_name='stringproperty',
            name='parent',
            field=models.ForeignKey(to='task.Property'),
        ),
        migrations.AddField(
            model_name='booleanproperty',
            name='parent',
            field=models.ForeignKey(to='task.Property'),
        ),
    ]
