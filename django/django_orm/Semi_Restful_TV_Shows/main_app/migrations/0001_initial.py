# Generated by Django 2.2.4 on 2021-05-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('network', models.CharField(max_length=225)),
                ('release_date', models.DateField()),
            ],
        ),
    ]