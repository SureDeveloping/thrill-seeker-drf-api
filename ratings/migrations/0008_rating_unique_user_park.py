# Generated by Django 5.0.6 on 2024-06-22 16:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0002_rename_author_park_user'),
        ('ratings', '0007_alter_rating_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'park'), name='unique_user_park'),
        ),
    ]
