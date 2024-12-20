# Generated by Django 3.2.7 on 2024-11-22 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_alter_message_options_alter_message_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectionrequest',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='connectionrequest',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
        migrations.RemoveField(
            model_name='room',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='roomfile',
            name='room',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
        migrations.DeleteModel(
            name='ConnectionRequest',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='RoomFile',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
