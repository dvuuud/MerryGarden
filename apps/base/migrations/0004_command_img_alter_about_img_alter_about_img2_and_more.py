# Generated by Django 5.0.3 on 2024-03-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_commands_contact_gallery_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='img',
            field=models.ImageField(default=1, upload_to='media3', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(upload_to='media1', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='about',
            name='img2',
            field=models.ImageField(upload_to='media2', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.ImageField(upload_to='media4', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Фото'),
        ),
    ]
