# Generated by Django 3.2.7 on 2021-10-29 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homedia', '0002_auto_20211029_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='usr',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='usr',
            new_name='user',
        ),
    ]
