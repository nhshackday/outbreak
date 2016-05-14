# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outbreak', '0005_auto_20160514_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Findings_abdominal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Findings abdominal',
            },
        ),
        migrations.CreateModel(
            name='Findings_cardiovascular',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Findings cardiovascular',
            },
        ),
        migrations.CreateModel(
            name='Findings_neurological',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Findings neurological',
            },
        ),
        migrations.CreateModel(
            name='Findings_oropharnyx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Findings oropharnyx',
            },
        ),
        migrations.CreateModel(
            name='Findings_respiratory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Findings respiratory',
            },
        ),
        migrations.RemoveField(
            model_name='examination',
            name='abdominal',
        ),
        migrations.RemoveField(
            model_name='examination',
            name='cardiovascular',
        ),
        migrations.RemoveField(
            model_name='examination',
            name='neurological',
        ),
        migrations.RemoveField(
            model_name='examination',
            name='oropharnyx',
        ),
        migrations.RemoveField(
            model_name='examination',
            name='respiratory',
        ),
        migrations.AddField(
            model_name='examination',
            name='abdominal_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='cardiovascular_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='neurological_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='oropharnyx_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='respiratory_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='abdominal_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Findings_abdominal', null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='cardiovascular_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Findings_cardiovascular', null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='neurological_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Findings_neurological', null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='oropharnyx_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Findings_oropharnyx', null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='respiratory_fk',
            field=models.ForeignKey(blank=True, to='outbreak.Findings_respiratory', null=True),
        ),
    ]
