# Generated by Django 4.0.5 on 2022-07-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='community/'),
        ),
        migrations.AddField(
            model_name='post',
            name='view_users',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/post/'),
        ),
    ]