# Generated by Django 4.0.5 on 2022-07-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='major2',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='register',
            field=models.IntegerField(null=True),
        ),
    ]
