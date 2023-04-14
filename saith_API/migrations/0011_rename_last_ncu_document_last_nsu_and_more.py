# Generated by Django 4.1.7 on 2023-04-14 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saith_API', '0010_rename_last_requisition_nfe_document_last_request_nfe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='last_ncu',
            new_name='last_nsu',
        ),
        migrations.AddField(
            model_name='nfe',
            name='operation_science_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
