# Generated by Django 2.2.1 on 2019-09-14 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20190914_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='decr',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='incr',
        ),
    ]
