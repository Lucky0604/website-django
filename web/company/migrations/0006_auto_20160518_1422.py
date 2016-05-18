# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20160516_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image1', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 14, 22, 18, 275706, tzinfo=utc)),
        ),
    ]
