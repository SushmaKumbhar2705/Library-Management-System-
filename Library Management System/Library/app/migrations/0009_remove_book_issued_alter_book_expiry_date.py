# Generated by Django 4.2.6 on 2023-10-31 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_book_issued_date_alter_book_expiry_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='issued',
        ),
        migrations.AlterField(
            model_name='book',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
    ]
