# Generated by Django 2.2.1 on 2019-09-14 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20190914_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcq',
            name='level',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ad_pass',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='number_of_questions',
        ),
    ]