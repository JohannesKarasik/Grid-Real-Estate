# Generated by Django 5.1.1 on 2024-10-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_user_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="background",
            field=models.ImageField(
                default="background_for_profile_info.jpg", null=True, upload_to=""
            ),
        ),
    ]
