# Generated by Django 3.1.7 on 2021-05-24 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0006_delete_index1'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=500)),
            ],
        ),
    ]
