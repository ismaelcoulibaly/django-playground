# Generated by Django 2.1.5 on 2020-12-01 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noyau', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netfeelex',
            name='Date_publie',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 23, 8, 57, 688235), verbose_name='Date publié'),
        ),
    ]
