# Generated by Django 2.2.14 on 2021-03-05 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebay', '0004_ebayaccount_oath_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebayaccount',
            name='oath_token',
            field=models.TextField(blank=True),
        ),
    ]
