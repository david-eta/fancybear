# Generated by Django 5.0.1 on 2024-02-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='quantity',
            field=models.DecimalField(decimal_places=5, max_digits=12),
        ),
    ]