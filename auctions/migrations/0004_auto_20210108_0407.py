# Generated by Django 3.1.5 on 2021-01-08 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='category',
            new_name='categories',
        ),
    ]
