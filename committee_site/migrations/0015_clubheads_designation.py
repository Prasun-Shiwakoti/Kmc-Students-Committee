# Generated by Django 3.1.7 on 2022-01-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0014_clubheads'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubheads',
            name='designation',
            field=models.CharField(choices=[('E', 'Executive'), ('P', 'Club President')], default='E', max_length=20),
        ),
    ]