# Generated by Django 3.2.5 on 2021-08-06 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballers', '0002_alter_players_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='players',
            new_name='Player',
        ),
    ]