# Generated by Django 5.0.3 on 2024-03-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_about_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilties',
            name='img',
            field=models.ImageField(default=1, upload_to='media9', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
