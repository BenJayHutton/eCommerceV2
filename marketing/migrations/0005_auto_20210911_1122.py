# Generated by Django 3.1.12 on 2021-09-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_auto_20201014_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingpreference',
            name='mailchimp_subscribed',
            field=models.BooleanField(default=True),
        ),
    ]