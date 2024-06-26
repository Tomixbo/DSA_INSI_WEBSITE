# Generated by Django 5.0.4 on 2024-05-20 07:47

import challenges.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Challenge",
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
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("author", models.CharField(blank=True, max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Alpha", "Alpha"),
                            ("Beta", "Beta"),
                            ("Gamma", "Gamma"),
                            ("Omega", "Omega"),
                        ],
                        default="Alpha",
                        max_length=10,
                    ),
                ),
                (
                    "difficulty",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
                    ),
                ),
                ("published", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Level",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "description_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=challenges.models.Level.upload_to_description_file,
                    ),
                ),
                (
                    "input_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=challenges.models.Level.upload_to_input_file,
                    ),
                ),
                (
                    "challenge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="levels",
                        to="challenges.challenge",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DefinedFile",
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
                ("name", models.CharField(max_length=100)),
                (
                    "input_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=challenges.models.DefinedFile.upload_to_input_file,
                    ),
                ),
                (
                    "output_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=challenges.models.DefinedFile.upload_to_output_file,
                    ),
                ),
                (
                    "level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="defined_files",
                        to="challenges.level",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Performance",
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
                ("solved", models.BooleanField(default=False)),
                ("description", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField()),
                (
                    "definedfile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="challenges.definedfile",
                    ),
                ),
            ],
        ),
    ]
