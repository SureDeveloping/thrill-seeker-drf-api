# Generated by Django 3.2.4 on 2024-07-06 15:15

import contact.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contactform_edit_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='edit_token',
        ),
        migrations.AddField(
            model_name='contactform',
            name='token',
            field=models.CharField(default=contact.models.generate_unique_token, max_length=36, unique=True),
        ),
    ]
