# Generated by Django 3.2.16 on 2023-01-20 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0005_auto_20230120_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='measurement_unit',
        ),
    ]
