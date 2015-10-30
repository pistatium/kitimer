# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayLog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('arrived_at', models.DateTimeField(null=True, blank=True)),
                ('left_at', models.DateTimeField(null=True, blank=True)),
                ('work_time', models.IntegerField(default=-1)),
                ('rest_time', models.IntegerField(default=60)),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='TimerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time', models.DateTimeField()),
                ('action_type', models.CharField(max_length=16, choices=[('arrived', '出社'), ('left', '退社')])),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='daylog',
            index_together=set([('date', 'user')]),
        ),
    ]
