# Generated by Django 4.1.2 on 2022-10-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cool', '0013_remove_biblestudymember_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblestudymember',
            name='sir_name',
            field=models.CharField(max_length=50),
        ),
    ]
