# Generated by Django 4.0.6 on 2022-08-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=1, max_length=10),
        ),
    ]
