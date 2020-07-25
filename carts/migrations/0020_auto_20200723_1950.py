# Generated by Django 2.2.14 on 2020-07-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0019_auto_20200723_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price_of_item',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='total',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=5),
        ),
    ]
