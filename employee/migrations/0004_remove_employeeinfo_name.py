# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employeeinfo_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeinfo',
            name='name',
        ),
    ]
