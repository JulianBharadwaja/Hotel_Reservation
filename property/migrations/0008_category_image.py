# Generated by Django 3.0.5 on 2020-04-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
    ]
