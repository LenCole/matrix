# Generated by Django 5.0.6 on 2024-05-25 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
