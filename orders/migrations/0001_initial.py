# Generated by Django 2.2.7 on 2019-11-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(max_length=64)),
                ('pizza_size', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Platters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platter_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SubToppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.ManyToManyField(blank=True, related_name='toppings', to='orders.Subs')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaToppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.ManyToManyField(blank=True, related_name='toppings', to='orders.Pizza')),
            ],
        ),
    ]
