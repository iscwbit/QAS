# Generated by Django 3.2.7 on 2022-06-09 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20220609_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='totoal_time',
            new_name='total_time',
        ),
        migrations.RemoveField(
            model_name='player',
            name='totoal_score',
        ),
    ]
