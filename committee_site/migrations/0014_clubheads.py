# Generated by Django 3.1.7 on 2022-01-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0013_auto_20220115_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubHeads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('club', models.CharField(max_length=100)),
                ('facebook_link', models.CharField(max_length=1000)),
                ('instagram_link', models.CharField(max_length=1000)),
                ('linkedin_link', models.CharField(max_length=1000)),
            ],
        ),
    ]
