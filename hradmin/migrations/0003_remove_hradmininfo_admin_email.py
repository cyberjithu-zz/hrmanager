# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hradmin', '0002_remove_hradmininfo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hradmininfo',
            name='admin_email',
        ),
    ]
