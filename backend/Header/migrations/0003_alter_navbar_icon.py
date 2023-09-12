# Generated by Django 4.2.4 on 2023-09-02 17:05

import Header.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('Header', '0002_alter_navbar_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='icon',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Header.models.upload_to_icons),
        ),
    ]
