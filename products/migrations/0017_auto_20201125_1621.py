# Generated by Django 2.2.14 on 2020-11-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20201125_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]