# Generated by Django 2.1.5 on 2019-02-18 18:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190219_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 18, 42, 36, 339747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 18, 42, 36, 339747, tzinfo=utc)),
        ),
    ]