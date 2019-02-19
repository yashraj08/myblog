# Generated by Django 2.1.5 on 2019-02-18 17:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(default=datetime.datetime(2019, 2, 18, 17, 7, 33, 362864, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(default=datetime.datetime(2019, 2, 18, 17, 7, 33, 361866, tzinfo=utc))),
                ('pub_time', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
