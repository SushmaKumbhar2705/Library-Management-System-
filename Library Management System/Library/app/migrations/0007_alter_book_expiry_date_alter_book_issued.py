# Generated by Django 4.2.6 on 2023-10-31 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_book_expiry_date_alter_book_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2023, 10, 31)),
        ),
        migrations.AlterField(
            model_name='book',
            name='issued',
            field=models.TimeField(default=datetime.datetime(2023, 10, 31, 5, 20, 50, 425879, tzinfo=datetime.timezone.utc)),
        ),
    ]