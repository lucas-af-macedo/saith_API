# Generated by Django 4.1.7 on 2023-04-14 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saith_API', '0011_rename_last_ncu_document_last_nsu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='document_number',
        ),
    ]
