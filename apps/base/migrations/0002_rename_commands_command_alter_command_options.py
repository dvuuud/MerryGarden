# Generated by Django 5.0.3 on 2024-03-23 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commands',
            new_name='Command',
        ),
        migrations.AlterModelOptions(
            name='command',
            options={'verbose_name_plural': 'Команда'},
        ),
    ]
