# Generated by Django 3.0.4 on 2020-05-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineFloorPass', '0015_remove_floorpass_latest_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='logdatetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
