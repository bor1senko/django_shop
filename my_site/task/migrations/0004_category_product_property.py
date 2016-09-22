# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20160725_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, to='task.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='task.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('product', models.ForeignKey(to='task.Product')),
            ],
            options={
                'ordering': ('key',),
            },
        ),
    ]
