# Generated by Django 3.1.12 on 2021-09-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20201112_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.FloatField(default=5.99),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]