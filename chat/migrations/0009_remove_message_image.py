# Generated by Django 4.0.1 on 2025-02-26 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_remove_message_image_msg_message_image_postimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
    ]
