# Generated by Django 4.2.6 on 2024-04-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0009_alter_portfolio_total_return_alter_portfolio_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='roi_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]