# Generated by Django 4.1.1 on 2022-12-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0011_host_tournament_tournament_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='host_tournament',
            name='Tournament_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
