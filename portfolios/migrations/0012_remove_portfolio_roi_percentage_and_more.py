# Generated by Django 4.2.6 on 2024-04-19 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0011_alter_portfolio_roi_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='roi_percentage',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='total_return',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='value',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='current_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='current_value',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='gains',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='roi',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='total_investment',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='average_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
