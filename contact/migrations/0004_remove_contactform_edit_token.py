# Generated by Django 3.2.4 on 2024-07-08 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_ensure_valid_uuids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='edit_token',
        ),
    ]
