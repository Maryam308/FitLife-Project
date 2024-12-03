# Generated by Django 4.1.13 on 2024-12-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "measurements",
            "0003_alter_measurement_options_remove_measurement_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="measurement",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="calves",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="chest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="hips",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="left_arm",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="right_arm",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="thighs",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="waist",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]
