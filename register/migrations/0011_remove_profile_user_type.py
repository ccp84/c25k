# Generated by Django 3.2.18 on 2023-03-20 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20230309_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
    ]
