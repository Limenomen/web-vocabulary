# Generated by Django 4.1.4 on 2023-01-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_media_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='articles', to='core.tag', verbose_name='Связанные теги'),
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Файл'),
        ),
    ]