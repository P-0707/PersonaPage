# Generated by Django 4.2.14 on 2024-08-21 14:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_certification_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='certification_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
