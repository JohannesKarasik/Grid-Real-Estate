# Generated by Django 5.1.1 on 2024-10-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0019_alter_user_avatar_alter_user_background"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="background",
            field=models.ImageField(
                default="default/background.jpg", null=True, upload_to=""
            ),
        ),
    ]
