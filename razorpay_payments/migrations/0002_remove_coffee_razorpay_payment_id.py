# Generated by Django 4.2.3 on 2023-07-09 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('razorpay_payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='razorpay_payment_id',
        ),
    ]
