# Generated by Django 4.1.1 on 2022-12-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0009_host_tournament_turfregistration_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_tournament',
            name='Tournament_rate',
            field=models.CharField(default='', max_length=50),
        ),
    ]
