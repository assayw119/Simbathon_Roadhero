# Generated by Django 4.0.5 on 2022-07-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]