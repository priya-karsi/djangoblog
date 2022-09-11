# Generated by Django 4.1.1 on 2022-09-11 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0002_alter_blog_activeyn'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='userID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
