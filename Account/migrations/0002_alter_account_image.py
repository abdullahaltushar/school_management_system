# Generated by Django 3.2.15 on 2023-03-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/profile'),
        ),
    ]
