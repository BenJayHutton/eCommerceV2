# Generated by Django 2.2.12 on 2020-07-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0014_auto_20200704_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
