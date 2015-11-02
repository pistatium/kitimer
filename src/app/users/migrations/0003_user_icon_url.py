# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon_url',
            field=models.TextField(blank=True),
        ),
    ]
