# Generated by Django 4.1.2 on 2022-10-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='adress',
            new_name='address',
        ),
    ]
