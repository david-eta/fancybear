# Generated by Django 4.2.6 on 2024-02-22 17:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolios', '0002_alter_portfolio_quantity'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='portfolio',
            unique_together={('user', 'stock')},
        ),
    ]