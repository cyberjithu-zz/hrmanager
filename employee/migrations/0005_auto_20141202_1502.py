# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_remove_employeeinfo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeinfo',
            old_name='active',
            new_name='active_flag',
        ),
    ]
