# Generated by Django 4.0.1 on 2025-02-24 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_message_image_msg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='image_msg',
        ),
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/message_pictures')),
                ('message', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chat.message')),
            ],
        ),
    ]
