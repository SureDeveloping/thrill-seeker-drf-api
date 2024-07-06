python
from django.db import migrations, models
import uuid

def gen_uuid(apps, schema_editor):
    ContactForm = apps.get_model('contact', 'ContactForm')
    for row in ContactForm.objects.all():
        row.new_edit_token = uuid.uuid4()
        row.save(update_fields=['new_edit_token'])

class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_rename_token_contactform_edit_token'),  # Stellen Sie sicher, dass dies die richtige vorherige Migration ist
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='new_edit_token',
            field=models.UUIDField(null=True, editable=False),
        ),
        migrations.RunPython(gen_uuid),
        migrations.AlterField(
            model_name='contactform',
            name='new_edit_token',
            field=models.UUIDField(default=uuid.uuid4, unique=True, editable=False),
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='edit_token',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='new_edit_token',
            new_name='edit_token',
        ),
    ]