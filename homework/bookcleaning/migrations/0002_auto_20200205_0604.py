# Generated by Django 3.0.2 on 2020-02-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcleaning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=12, verbose_name='Contact'),
        ),
    ]
