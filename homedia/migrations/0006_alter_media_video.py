# Generated by Django 3.2.7 on 2021-10-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homedia', '0005_auto_20211029_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]
