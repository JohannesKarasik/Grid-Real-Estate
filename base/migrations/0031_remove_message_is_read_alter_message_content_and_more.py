# Generated by Django 5.1.1 on 2024-10-10 20:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0030_alter_connection_unique_together_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="is_read",
        ),
        migrations.AlterField(
            model_name="message",
            name="content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="message",
            name="recipient",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_messages",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="message",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
