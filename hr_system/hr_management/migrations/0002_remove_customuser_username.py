# Generated by Django 4.2.6 on 2023-10-13 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
