# Generated by Django 2.0.13 on 2019-08-18 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('pub_date', models.DateField(default=datetime.datetime.today)),
                ('body', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
