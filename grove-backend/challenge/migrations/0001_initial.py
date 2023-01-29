# Generated by Django 4.1.5 on 2023-01-29 07:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyChallenge",
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
                (
                    "xp",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("desc", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UserChallenge",
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
                (
                    "xp",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("desc", models.CharField(default="", max_length=255)),
                (
                    "dst",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dst",
                        to="users.user",
                    ),
                ),
                (
                    "src",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="src",
                        to="users.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DailyChallengeCompletion",
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
                (
                    "daily",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="challenge.dailychallenge",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]