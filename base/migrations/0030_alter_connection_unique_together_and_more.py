# Generated by Django 5.1.1 on 2024-10-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0029_alter_connection_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="connection",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="connection",
            constraint=models.UniqueConstraint(
                fields=("user", "connection"), name="unique_connection"
            ),
        ),
    ]
