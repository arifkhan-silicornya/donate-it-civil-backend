# Generated by Django 3.2.12 on 2023-09-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeverification',
            name='createDate',
            field=models.CharField(default='09/12/23 07:40:40', max_length=300),
        ),
        migrations.AlterField(
            model_name='codeverification',
            name='expiredDate',
            field=models.CharField(default='09/12/23 07:55:40', max_length=300),
        ),
    ]
