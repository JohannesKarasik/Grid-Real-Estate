# Generated by Django 5.1.1 on 2024-10-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0021_alter_user_background"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="background",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
