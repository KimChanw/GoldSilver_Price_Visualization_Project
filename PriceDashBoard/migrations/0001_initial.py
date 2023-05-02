# Generated by Django 4.1 on 2023-05-02 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MatrialsModel",
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
                ("matrial_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="MatrialsPriceModel",
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
                ("date", models.DateField()),
                ("price", models.FloatField()),
                (
                    "matrial_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="PriceDashBoard.matrialsmodel",
                    ),
                ),
            ],
        ),
    ]