# Generated by Django 5.0.2 on 2024-02-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("favorites", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="favorite",
            name="id",
        ),
        migrations.AlterField(
            model_name="favorite",
            name="stock",
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
