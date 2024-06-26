# Generated by Django 3.1.7 on 2021-07-19 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee_site', '0011_notice_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=100)),
                ('Message', models.TextField(default='')),
                ('Stars', models.IntegerField()),
                ('Image', models.ImageField(upload_to='FeedbackImages')),
            ],
        ),
    ]
