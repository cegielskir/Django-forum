# Generated by Django 2.0.6 on 2018-06-19 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180619_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 18, 14, 10, 572084)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 18, 14, 10, 571085)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 18, 14, 10, 572084)),
        ),
    ]
