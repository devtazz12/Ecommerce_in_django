# Generated by Django 4.2.4 on 2023-10-13 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='profile_img/user.jfif', upload_to='profile_pic'),
        ),
    ]
