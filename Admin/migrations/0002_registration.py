# Generated by Django 4.1.1 on 2022-11-11 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Admin", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=100)),
                ("user_email", models.CharField(default="", max_length=20)),
                ("user_pass", models.CharField(max_length=50)),
                ("user_phone", models.CharField(max_length=12)),
                ("user_status", models.IntegerField()),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Admin.role"
                    ),
                ),
            ],
        ),
    ]
