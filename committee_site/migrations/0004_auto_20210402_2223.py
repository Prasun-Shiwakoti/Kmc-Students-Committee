# Generated by Django 3.1.7 on 2021-04-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0003_auto_20210402_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='Description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Heading',
            field=models.CharField(default='', max_length=100),
        ),
    ]
