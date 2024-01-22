# Generated by Django 5.0.1 on 2024-01-22 19:30

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=True, populate_from='title'),
        ),
    ]
