# Generated by Django 2.2.5 on 2019-09-19 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='address',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='genre',
        ),
    ]
