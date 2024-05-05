# Generated by Django 5.0.4 on 2024-05-04 12:11

import challenges.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0003_level_description_file_alter_level_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="level",
            name="description_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=challenges.models.Level.upload_to_description_file,
            ),
        ),
        migrations.AlterField(
            model_name="level",
            name="input_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=challenges.models.Level.upload_to_input_file,
            ),
        ),
    ]