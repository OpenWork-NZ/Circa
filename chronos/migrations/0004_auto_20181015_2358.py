# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('chronos', '0003_auto_20181015_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dating',
            name='changed_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
