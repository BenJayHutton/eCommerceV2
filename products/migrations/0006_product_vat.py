# Generated by Django 2.2.14 on 2020-10-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201014_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
