# Generated by Django 3.2.7 on 2022-06-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_raking'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='totoal_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='คะแนนรวม'),
        ),
        migrations.AddField(
            model_name='player',
            name='totoal_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='เวลารวม'),
        ),
    ]
