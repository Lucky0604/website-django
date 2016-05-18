# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='authors',
        ),
        migrations.AlterField(
            model_name='content',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 14, 22, 18, 273725, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
