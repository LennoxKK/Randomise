# Generated by Django 4.0.6 on 2022-07-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='The_member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_study', models.IntegerField(max_length=4)),
                ('gender', models.CharField(choices=[('MALE', 'FEMALE')], max_length=4)),
                ('leader_status', models.BooleanField(default=False)),
                ('leader_pre_status', models.BooleanField(default=False)),
            ],
        ),
    ]
