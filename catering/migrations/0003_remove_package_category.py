# Generated by Django 3.1.7 on 2021-05-22 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0002_auto_20210522_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='category',
        ),
    ]