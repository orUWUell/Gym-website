# Generated by Django 4.0.1 on 2025-02-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_remove_message_imagemsg_message_image_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image_msg',
            field=models.FileField(blank=True, upload_to='images/message_pictures'),
        ),
    ]
