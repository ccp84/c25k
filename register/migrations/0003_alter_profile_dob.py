# Generated by Django 3.2.18 on 2023-02-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20230228_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
