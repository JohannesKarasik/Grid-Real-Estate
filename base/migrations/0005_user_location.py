# Generated by Django 5.1.1 on 2024-10-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_user_occupation"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.TextField(null=True),
        ),
    ]
