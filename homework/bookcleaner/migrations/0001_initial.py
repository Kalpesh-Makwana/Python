# Generated by Django 3.0.2 on 2020-02-06 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookcleaning', '0004_city_cleaner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingCleanerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timeslot', models.IntegerField(null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookcleaning.City')),
                ('cleaner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookcleaning.Cleaner')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
