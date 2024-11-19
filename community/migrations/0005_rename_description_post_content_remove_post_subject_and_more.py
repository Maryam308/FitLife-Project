# Generated by Django 4.1.13 on 2024-11-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0004_comment_commentlike"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="description",
            new_name="content",
        ),
        migrations.RemoveField(
            model_name="post",
            name="subject",
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[
                    ("workout", "Workout"),
                    ("diet", "Diet"),
                    ("transformation", "Transformation"),
                    ("general", "General"),
                ],
                default="general",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.CharField(default="Default Title", max_length=255),
        ),
    ]
