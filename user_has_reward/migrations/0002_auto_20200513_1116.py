# Generated by Django 3.0.4 on 2020-05-13 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_has_reward', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_has_reward',
            name='finish_time',
            field=models.DateTimeField(),
        ),
    ]
