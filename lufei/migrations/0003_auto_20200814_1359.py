# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-08-14 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lufei', '0002_auto_20200813_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '线上'), (1, '下线'), (2, '预上线')], default=0),
        ),
        migrations.AlterField(
            model_name='courseoutline',
            name='course_detail',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outlines', to='lufei.CourseDetail'),
        ),
    ]