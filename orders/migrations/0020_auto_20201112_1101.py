# Generated by Django 2.2.14 on 2020-11-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20201031_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=5.99, max_digits=10),
        ),
    ]