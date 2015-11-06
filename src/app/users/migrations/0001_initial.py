# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('slack_name', models.CharField(max_length=32, blank=True)),
                ('status', models.CharField(default='active', max_length=16, choices=[('active', 'Active'), ('inactive', 'Inactive')])),
                ('icon_url', models.URLField(blank=True)),
                ('access_key', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
