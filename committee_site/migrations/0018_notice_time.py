# Generated by Django 4.0.1 on 2022-01-21 09:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0017_auto_20220115_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
