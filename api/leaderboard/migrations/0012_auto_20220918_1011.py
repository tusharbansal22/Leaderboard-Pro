# Generated by Django 3.2.4 on 2022-09-18 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0011_remove_codechefuser_last_activity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='githubuser',
            options={},
        ),
        migrations.RemoveField(
            model_name='githubuser',
            name='rank',
        ),
    ]
