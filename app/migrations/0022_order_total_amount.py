# Generated by Django 4.2.4 on 2023-10-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]