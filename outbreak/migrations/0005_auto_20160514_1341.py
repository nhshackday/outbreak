# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outbreak', '0004_auto_20160514_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examination',
            old_name='dehydrated',
            new_name='dehydration',
        ),
    ]
