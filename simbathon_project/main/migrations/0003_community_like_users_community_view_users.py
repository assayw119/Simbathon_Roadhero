# Generated by Django 4.0.5 on 2022-07-08 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_community_image_post_view_users_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='like_users',
            field=models.ManyToManyField(related_name='community_like_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='community',
            name='view_users',
            field=models.IntegerField(default=0),
        ),
    ]
