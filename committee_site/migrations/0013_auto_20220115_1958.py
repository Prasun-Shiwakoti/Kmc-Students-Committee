# Generated by Django 3.1.7 on 2022-01-15 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0012_review'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='GalleryPhotos',
        ),
    ]