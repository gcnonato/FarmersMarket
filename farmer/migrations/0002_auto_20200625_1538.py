# Generated by Django 3.0.7 on 2020-06-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerinfo',
            name='telephone_number',
            field=models.IntegerField(default='0775058319', unique=True),
        ),
    ]
