# Generated by Django 4.1 on 2022-09-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_text_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='likesCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='text',
            name='likes',
            field=models.CharField(default='', max_length=100),
        ),
    ]
