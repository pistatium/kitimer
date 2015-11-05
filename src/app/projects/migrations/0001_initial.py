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
                ('name', models.CharField(serialize=False, primary_key=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('commit_rate', models.FloatField(default=1.0)),
                ('memo', models.TextField(blank=True)),
                ('day_log', models.ForeignKey(related_name='projects', to='timer.DayLog')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
    ]
