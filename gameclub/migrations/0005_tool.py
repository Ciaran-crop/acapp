# Generated by Django 3.2.8 on 2022-12-02 04:04

from django.db import migrations, models
import gameclub.models.tools


class Migration(migrations.Migration):

    dependencies = [
        ('gameclub', '0004_alter_usergameinfo_last_play'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('types', models.CharField(blank=True, max_length=128)),
                ('photo', models.ImageField(blank=True, upload_to=gameclub.models.tools.tool_directory_path)),
                ('url', models.URLField(blank=True, max_length=128)),
            ],
        ),
    ]
