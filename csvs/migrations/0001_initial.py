# Generated by Django 4.0.6 on 2022-07-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csvs')),
                ('uploaded', models.DateField(auto_now_add=True)),
                ('activated', models.BooleanField(default=True)),
            ],
        ),
    ]
