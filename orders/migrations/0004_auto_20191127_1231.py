# Generated by Django 2.2.7 on 2019-11-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_price_food_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='food_type',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Pasta', 'Pasta'), ('Salad', 'Salad'), ('Platter', 'Platter'), ('Sub', 'Sub'), ('Topping', 'Topping')], max_length=65),
        ),
    ]
