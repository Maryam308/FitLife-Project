# Generated by Django 4.1.13 on 2024-12-07 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_fitnessclass_capacity_fitnessclass_location'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='fitnessclass',
            table='fitness_classes',
        ),
        migrations.AlterModelTable(
            name='userclass',
            table='user_classes',
        ),
    ]
