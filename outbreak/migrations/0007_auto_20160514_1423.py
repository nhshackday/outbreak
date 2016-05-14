# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0017_auto_20160509_1645'),
        ('outbreak', '0006_auto_20160514_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('dose', models.CharField(max_length=255, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('route_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('drug_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('frequency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_outbreak_drugs_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('drug_fk', models.ForeignKey(blank=True, to='opal.Drug', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('frequency_fk', models.ForeignKey(blank=True, to='opal.Drugfreq', null=True)),
                ('route_fk', models.ForeignKey(blank=True, to='opal.Drugroute', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated_outbreak_drugs_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('dose', models.CharField(max_length=255, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('route_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('drug_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('frequency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('feeding_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_outbreak_feeding_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('drug_fk', models.ForeignKey(blank=True, to='opal.Drug', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Feeding_treatments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Feeding Treatments',
            },
        ),
        migrations.CreateModel(
            name='Fluid_treatments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Fluid Treatments',
            },
        ),
        migrations.CreateModel(
            name='Fluids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('dose', models.CharField(max_length=255, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('route_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('drug_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('frequency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('fluids_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_outbreak_fluids_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('drug_fk', models.ForeignKey(blank=True, to='opal.Drug', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('fluids_fk', models.ForeignKey(blank=True, to='outbreak.Fluid_treatments', null=True)),
                ('frequency_fk', models.ForeignKey(blank=True, to='opal.Drugfreq', null=True)),
                ('route_fk', models.ForeignKey(blank=True, to='opal.Drugroute', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated_outbreak_fluids_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='drug_fk',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='frequency_fk',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='route_fk',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='Treatment',
        ),
        migrations.AddField(
            model_name='feeding',
            name='feeding_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Feeding_treatments', null=True),
        ),
        migrations.AddField(
            model_name='feeding',
            name='frequency_fk',
            field=models.ForeignKey(blank=True, to='opal.Drugfreq', null=True),
        ),
        migrations.AddField(
            model_name='feeding',
            name='route_fk',
            field=models.ForeignKey(blank=True, to='opal.Drugroute', null=True),
        ),
        migrations.AddField(
            model_name='feeding',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_outbreak_feeding_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
