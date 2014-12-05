# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_id', models.IntegerField(max_length=100)),
                ('message_body', models.CharField(max_length=2000)),
                ('date_send', models.DateTimeField(verbose_name=b'Send Datetime')),
                ('receiver', models.ForeignKey(related_name='message receiver', default=b'', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='message sender', default=b'', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
