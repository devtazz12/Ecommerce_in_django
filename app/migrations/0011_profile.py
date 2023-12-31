# Generated by Django 4.2.4 on 2023-10-12 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_alter_cart_quantity_based_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(default='profile_img/user.jfif', upload_to='profile_img')),
                ('date_of_birth', models.DateField(blank=True, default='N/A', null=True)),
                ('phone_number', models.CharField(default='N/A', max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
