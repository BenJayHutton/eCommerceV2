# Generated by Django 2.2.12 on 2020-07-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0012_auto_20200702_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='session_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
