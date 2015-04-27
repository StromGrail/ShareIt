# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=500)),
                ('upsswd', models.CharField(max_length=500, serialize=False, primary_key=True)),
                ('umail', models.CharField(max_length=500)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
