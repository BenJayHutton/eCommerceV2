# Generated by Django 2.2.14 on 2021-03-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('blog', '0004_auto_20210304_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
    ]
