# Generated by Django 2.2.14 on 2020-07-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0017_auto_20200723_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price_of_item',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]