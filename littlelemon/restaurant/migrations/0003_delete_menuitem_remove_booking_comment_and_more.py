# Generated by Django 5.0 on 2023-12-28 12:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menuitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guest_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='menu_item_description',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='Booking', max_length=255),
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default='Menu', max_length=255),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
