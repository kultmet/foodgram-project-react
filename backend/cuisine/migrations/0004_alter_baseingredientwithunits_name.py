# Generated by Django 3.2.16 on 2023-01-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0003_alter_baseingredientwithunits_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseingredientwithunits',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название ингредиента'),
        ),
    ]
