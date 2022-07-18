# Generated by Django 4.0.6 on 2022-07-18 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Conformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'conformations',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('businss_hours', models.CharField(max_length=20, null=True)),
                ('url', models.URLField(null=True)),
                ('atitude', models.DecimalField(decimal_places=14, default=0.0, max_digits=16)),
                ('longitude', models.DecimalField(decimal_places=14, default=0.0, max_digits=17)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.category')),
                ('conformation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.conformation')),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'db_table': 'restaurant_images',
            },
        ),
        migrations.CreateModel(
            name='menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.maincategory'),
        ),
    ]
