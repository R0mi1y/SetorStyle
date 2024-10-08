# Generated by Django 5.1 on 2024-09-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sector', '0008_banner_size_description_banner_size_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='align',
            field=models.TextField(choices=[('flex-start', 'Início'), ('flex-end', 'Fim'), ('center', 'Centro')], default='flex-start', verbose_name='Alinhamento horizontal'),
        ),
    ]
