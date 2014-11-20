# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('employee_id', models.IntegerField(max_length=5)),
                ('employee_email', models.EmailField(max_length=75)),
                ('date_of_join', models.DateTimeField(verbose_name=b'date joined')),
                ('addressline_1', models.CharField(max_length=100)),
                ('addressline_2', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('phone_mobile', models.CharField(max_length=14)),
                ('phone_home', models.CharField(max_length=14)),
                ('department', models.CharField(max_length=200)),
                ('working_on', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
