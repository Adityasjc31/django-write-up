# Generated by Django 4.1 on 2022-09-15 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_privacy_text_privacy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='Privacy',
            new_name='privacy',
        ),
    ]
