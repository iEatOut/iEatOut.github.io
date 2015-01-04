# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ieatout', '0002_auto_20150104_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='RestaurantPreference',
            new_name='state',
        ),
    ]
