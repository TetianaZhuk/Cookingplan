# Generated by Django 4.0.3 on 2022-06-19 21:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_alter_meal_slug_alter_mealcategory_slug'),
        ('menu', '0004_remove_day_breakfast_remove_day_dinner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinner',
            name='day',
        ),
        migrations.RemoveField(
            model_name='dinner',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='launch',
            name='day',
        ),
        migrations.RemoveField(
            model_name='launch',
            name='meal',
        ),
        migrations.AddField(
            model_name='day',
            name='breakfast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breakfast', to='meals.meal'),
        ),
        migrations.AddField(
            model_name='day',
            name='dinner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dinner', to='meals.meal'),
        ),
        migrations.AddField(
            model_name='day',
            name='launch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='launch', to='meals.meal'),
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 19, 21, 9, 26, 953283, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Breakfast',
        ),
        migrations.DeleteModel(
            name='Dinner',
        ),
        migrations.DeleteModel(
            name='Launch',
        ),
    ]