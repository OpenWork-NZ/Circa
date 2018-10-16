# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chronos', '0002_auto_20181004_0223_squashed_0004_auto_20181005_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('changed_at', models.DateField(auto_now=True)),
                ('justification', models.TextField()),
                ('reference', models.URLField(null=True, blank=True)),
                ('start', models.DateField(null=True, blank=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('changed_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='end',
        ),
        migrations.RemoveField(
            model_name='album',
            name='href',
        ),
        migrations.RemoveField(
            model_name='album',
            name='start',
        ),
        migrations.AddField(
            model_name='dating',
            name='for_album',
            field=models.ForeignKey(to='chronos.Album'),
        ),
    ]
