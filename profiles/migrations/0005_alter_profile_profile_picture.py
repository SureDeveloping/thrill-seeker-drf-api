# Generated by Django 3.2.4 on 2024-07-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='../profile_default_edit7h', upload_to='profile_pictures/'),
        ),
    ]
