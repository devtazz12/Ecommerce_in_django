# Generated by Django 4.2.4 on 2023-10-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, default='00-00-000', null=True),
        ),
    ]