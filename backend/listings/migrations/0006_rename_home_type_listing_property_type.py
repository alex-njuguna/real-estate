# Generated by Django 5.0.1 on 2024-01-22 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_home_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='home_type',
            new_name='property_type',
        ),
    ]