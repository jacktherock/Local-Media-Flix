# Generated by Django 3.2.7 on 2021-10-29 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homedia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='user',
            new_name='usr',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='user',
            new_name='usr',
        ),
    ]