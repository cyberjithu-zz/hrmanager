# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hradmin', '0003_remove_hradmininfo_admin_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hradmininfo',
            old_name='active',
            new_name='active_flag',
        ),
    ]
