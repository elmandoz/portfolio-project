# Generated by Django 2.0.13 on 2019-08-19 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190819_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]