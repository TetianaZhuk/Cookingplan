# Generated by Django 4.0.3 on 2022-06-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_alter_mealingredients_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealingredients',
            name='qty',
            field=models.IntegerField(verbose_name='Количество'),
        ),
    ]
