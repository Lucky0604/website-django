# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('cultureid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('culture_item', models.CharField(max_length=200)),
                ('culture_tag', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Culture',
                'verbose_name_plural': 'Culture',
            },
        ),
        migrations.CreateModel(
            name='CultureContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('culture_headline', models.CharField(max_length=200)),
                ('culture_bodytext', tinymce.models.HTMLField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pub_date', models.DateTimeField(null=True, blank=True)),
                ('authors', models.ManyToManyField(to='company.Author')),
                ('culture_name', models.ForeignKey(db_column='culture_name', to='culture.Culture')),
            ],
            options={
                'verbose_name': 'Culture Content',
                'verbose_name_plural': 'Culture Content',
            },
        ),
    ]
