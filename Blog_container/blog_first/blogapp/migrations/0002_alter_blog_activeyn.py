# Generated by Django 4.1.1 on 2022-09-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='activeYN',
            field=models.IntegerField(default=1),
        ),
    ]