# Generated by Django 3.1.5 on 2021-06-15 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='send_to',
        ),
    ]
