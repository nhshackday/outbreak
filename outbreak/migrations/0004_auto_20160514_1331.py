# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0017_auto_20160509_1645'),
        ('outbreak', '0003_patienthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('lymphadenopathy', models.CharField(max_length=20, null=True, blank=True)),
                ('lymphadenopathy_details', models.CharField(max_length=255, null=True, blank=True)),
                ('jaundice', models.CharField(max_length=20, blank=True)),
                ('dehydrated', models.CharField(max_length=20, blank=True)),
                ('rash', models.CharField(max_length=20, blank=True)),
                ('cardiovascular', models.CharField(max_length=255, null=True, blank=True)),
                ('respiratory', models.CharField(max_length=255, null=True, blank=True)),
                ('abdominal', models.CharField(max_length=255, null=True, blank=True)),
                ('oropharnyx', models.CharField(max_length=255, null=True, blank=True)),
                ('neurological', models.CharField(max_length=255, null=True, blank=True)),
                ('other_findings', models.CharField(max_length=255, null=True, blank=True)),
                ('rash_type_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('rash_distribution_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_outbreak_examination_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Findings_rash_distribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Findings rash distribution',
            },
        ),
        migrations.CreateModel(
            name='Findings_rash_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Findings rash type',
            },
        ),
        migrations.AddField(
            model_name='examination',
            name='rash_distribution_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Findings_rash_distribution', null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='rash_type_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Findings_rash_type', null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_outbreak_examination_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
