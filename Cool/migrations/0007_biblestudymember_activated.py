# Generated by Django 4.0.6 on 2022-09-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cool', '0006_biblestudymember'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblestudymember',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
