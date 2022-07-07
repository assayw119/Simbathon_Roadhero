# Generated by Django 4.0.5 on 2022-07-07 18:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_post_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_users',
            field=models.ManyToManyField(related_name='view_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]