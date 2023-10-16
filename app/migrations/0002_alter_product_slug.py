# Generated by Django 4.2.4 on 2023-10-05 01:57

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]