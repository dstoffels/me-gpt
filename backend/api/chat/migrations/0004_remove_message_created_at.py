# Generated by Django 5.0.3 on 2024-03-06 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
    ]
