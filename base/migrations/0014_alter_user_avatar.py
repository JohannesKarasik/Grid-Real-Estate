# Generated by Django 5.1.1 on 2024-10-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0013_rename_name_profile_full_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, default="default/avatar.svg", null=True, upload_to=""
            ),
        ),
    ]
