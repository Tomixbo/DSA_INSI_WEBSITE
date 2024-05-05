# Generated by Django 5.0.4 on 2024-05-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0008_challenge_category_challenge_difficulty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="category",
            field=models.CharField(
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
    ]
