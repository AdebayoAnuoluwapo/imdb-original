# Generated by Django 2.2.5 on 2020-06-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200622_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielinks',
            name='type',
            field=models.CharField(choices=[('D', 'DOWNLOAD_LINK'), ('W', 'WATCH_LINK')], max_length=1),
        ),
    ]
