# Generated by Django 4.1.7 on 2023-04-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saith_API', '0002_alter_sessions_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
