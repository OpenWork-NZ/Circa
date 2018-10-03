# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField(null=True)),
                ('href', models.URLField(null=True)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
            ],
        ),
    ]
