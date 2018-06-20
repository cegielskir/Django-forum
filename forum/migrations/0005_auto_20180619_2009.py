# Generated by Django 2.0.6 on 2018-06-19 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20180619_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='answers',
            field=models.ManyToManyField(to='forum.Answer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 20, 9, 17, 681024)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 20, 9, 17, 680025)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 20, 9, 17, 681024)),
        ),
    ]