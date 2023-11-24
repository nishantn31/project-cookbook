# Generated by Django 4.2.6 on 2023-11-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vege", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                ("recipe_name", models.CharField(max_length=100)),
                ("recipe_description", models.TextField()),
                ("recipe_image", models.ImageField(upload_to="recipe")),
            ],
        ),
        migrations.DeleteModel(
            name="Receipe",
        ),
    ]
