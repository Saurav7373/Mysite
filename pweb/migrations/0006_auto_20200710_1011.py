# Generated by Django 3.0.6 on 2020-07-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pweb', '0005_auto_20200710_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='dob',
            field=models.DateTimeField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='dob',
            field=models.DateTimeField(default=''),
        ),
    ]
