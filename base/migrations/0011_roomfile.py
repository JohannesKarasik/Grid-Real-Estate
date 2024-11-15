# Generated by Django 5.1.1 on 2024-10-05 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_alter_room_postimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="room_files/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="base.room",
                    ),
                ),
            ],
        ),
    ]
