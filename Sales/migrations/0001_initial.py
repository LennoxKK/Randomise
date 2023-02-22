# Generated by Django 4.0.6 on 2022-07-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('TV', 'tv'), ('IPAD', 'ipad'), ('PLAYSATTION', 'playstation')], max_length=11)),
                ('quantity', models.PositiveIntegerField()),
                ('total', models.FloatField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]