# Generated by Django 3.1.7 on 2021-05-22 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='package',
            name='subcategory',
        ),
    ]
