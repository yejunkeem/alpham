# Generated by Django 4.1.5 on 2023-01-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
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
                ("title", models.CharField(max_length=20, null=True)),
                ("content", models.TextField()),
                ("writer", models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
