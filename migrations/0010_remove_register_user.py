# Generated by Django 5.0.5 on 2024-05-13 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
    ]