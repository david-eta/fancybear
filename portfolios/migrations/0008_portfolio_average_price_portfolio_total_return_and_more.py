# Generated by Django 4.2.6 on 2024-04-01 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0007_alter_portfolio_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='average_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='total_return',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
