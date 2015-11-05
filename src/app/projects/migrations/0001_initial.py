# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=128, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commit_rate', models.FloatField(default=1.0)),
                ('memo', models.TextField(blank=True)),
                ('day_log', models.ForeignKey(to='timer.DayLog', related_name='project_logs')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
    ]
