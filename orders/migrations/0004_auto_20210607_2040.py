# Generated by Django 3.1.4 on 2021-06-07 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210607_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 20, 40, 42, 80557)),
        ),
    ]