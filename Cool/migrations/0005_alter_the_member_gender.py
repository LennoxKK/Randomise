# Generated by Django 4.0.6 on 2022-07-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cool', '0004_alter_the_member_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='the_member',
            name='gender',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=6),
        ),
    ]
