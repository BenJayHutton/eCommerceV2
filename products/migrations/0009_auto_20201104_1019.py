# Generated by Django 2.2.14 on 2020-11-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201103_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfile',
            name='free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productfile',
            name='user_required',
            field=models.BooleanField(default=False),
        ),
    ]
