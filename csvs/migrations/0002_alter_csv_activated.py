# Generated by Django 4.0.6 on 2022-08-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]