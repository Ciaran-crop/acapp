# Generated by Django 3.2.8 on 2022-11-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_player_back_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=1500),
        ),
    ]