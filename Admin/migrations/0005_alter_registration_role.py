# Generated by Django 4.1.2 on 2022-11-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_alter_registration_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='role',
            field=models.CharField(default='team', max_length=100),
        ),
    ]
