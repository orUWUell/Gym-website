# Generated by Django 4.0.1 on 2025-03-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_remove_message_image_message_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/message_pictures'),
        ),
    ]
