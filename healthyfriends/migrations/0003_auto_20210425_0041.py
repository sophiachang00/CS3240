# Generated by Django 3.1.6 on 2021-04-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthyfriends', '0002_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]