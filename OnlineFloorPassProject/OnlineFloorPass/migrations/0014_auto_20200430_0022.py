# Generated by Django 3.0.4 on 2020-04-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineFloorPass', '0013_auto_20200425_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorpass',
            name='supervisor_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]