# Generated by Django 3.2.5 on 2021-07-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0006_feedbacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='HeaderImages')),
            ],
        ),
    ]
