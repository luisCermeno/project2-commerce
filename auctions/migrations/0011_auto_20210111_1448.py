# Generated by Django 3.1.5 on 2021-01-11 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210111_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='listing',
            new_name='listings',
        ),
    ]