# Generated by Django 2.2.4 on 2021-05-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210522_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='old dojo', max_length=255),
        ),
    ]
