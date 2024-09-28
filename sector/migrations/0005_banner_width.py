# Generated by Django 5.1 on 2024-09-28 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sector', '0004_remove_banner_position_banner_align_banner_justify'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='width',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)], verbose_name='Largura'),
        ),
    ]
