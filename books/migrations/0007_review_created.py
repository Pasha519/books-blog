# Generated by Django 4.0.6 on 2022-08-14 14:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
