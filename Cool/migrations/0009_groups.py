# Generated by Django 4.0.6 on 2022-09-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cool', '0008_remove_biblestudymember_activated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
    ]
