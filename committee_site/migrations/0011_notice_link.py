# Generated by Django 3.2.5 on 2021-07-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0010_alter_headerimages_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='Link',
            field=models.URLField(blank=True),
        ),
    ]
