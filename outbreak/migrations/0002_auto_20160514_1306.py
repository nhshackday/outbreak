# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0017_auto_20160509_1645'),
        ('outbreak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentingSymptoms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('duration', models.CharField(max_length=255, null=True, blank=True)),
                ('details', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_outbreak_presentingsymptoms_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('symptoms', models.ManyToManyField(related_name='presenting_complaints', to='opal.Symptom')),
                ('updated_by', models.ForeignKey(related_name='updated_outbreak_presentingsymptoms_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.AddField(
            model_name='demographics',
            name='fuzzy_age',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
