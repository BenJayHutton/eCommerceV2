# Generated by Django 2.2.14 on 2020-07-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0021_auto_20200725_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price_of_item',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]