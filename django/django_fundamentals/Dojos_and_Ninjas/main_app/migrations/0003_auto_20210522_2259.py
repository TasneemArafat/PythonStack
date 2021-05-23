# Generated by Django 2.2.4 on 2021-05-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210522_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='ninja',
            name='first_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ninja',
            name='last_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
