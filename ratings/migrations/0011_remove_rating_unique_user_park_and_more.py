# Generated by Django 5.0.6 on 2024-06-22 16:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0002_rename_author_park_user'),
        ('ratings', '0010_rating_unique_user_park'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='rating',
            name='unique_user_park',
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'park')},
        ),
    ]
