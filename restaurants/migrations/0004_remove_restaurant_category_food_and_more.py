# Generated by Django 4.0.6 on 2022-07-22 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_remove_restaurant_category_restaurant_category_food_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='category_food',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='category_region',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.category'),
        ),
    ]
