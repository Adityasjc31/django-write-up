# Generated by Django 4.1 on 2022-09-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_text_privacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='temptext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(max_length=9999999999999999999999999999999999)),
            ],
        ),
    ]
