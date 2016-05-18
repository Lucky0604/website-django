# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0002_auto_20160518_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 14, 43, 36, 69128, tzinfo=utc)),
        ),
    ]
