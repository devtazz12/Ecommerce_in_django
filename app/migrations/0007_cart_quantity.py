# Generated by Django 4.2.4 on 2023-10-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_cart_order_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
