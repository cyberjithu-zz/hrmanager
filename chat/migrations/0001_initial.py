# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_id', models.IntegerField(max_length=100)),
                ('message', models.CharField(max_length=2000)),
                ('date_send', models.DateTimeField(verbose_name=b'Send Datetime')),
                ('sender_id', models.IntegerField(max_length=5)),
                ('sender_name', models.CharField(max_length=200)),
                ('receiver_id', models.IntegerField(max_length=5)),
                ('receiver_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
