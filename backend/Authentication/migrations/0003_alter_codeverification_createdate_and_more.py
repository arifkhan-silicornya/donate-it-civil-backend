# Generated by Django 4.2.4 on 2023-09-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_auto_20230906_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeverification',
            name='createDate',
            field=models.CharField(default='09/06/23 16:04:21', max_length=300),
        ),
        migrations.AlterField(
            model_name='codeverification',
            name='expiredDate',
            field=models.CharField(default='09/06/23 16:19:21', max_length=300),
        ),
    ]
