# Generated by Django 4.0.3 on 2022-04-03 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=12)),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
                ('country', models.CharField(choices=[('uk', 'United Kingdom'), ('usa', 'United States of America')], default='uk', max_length=120)),
                ('billing_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.billingprofile')),
            ],
        ),
    ]
