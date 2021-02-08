# Generated by Django 3.1 on 2021-02-08 10:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20210208_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('fas', 'Fashion'), ('app', 'Home and Appliances'), ('book', 'Books and Magazines')], max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 10, 19, 23, 739792, tzinfo=utc), verbose_name='date of release'),
        ),
    ]
