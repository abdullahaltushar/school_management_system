# Generated by Django 3.2.15 on 2023-03-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanage', '0004_alter_subjects_teacher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='total_result',
            field=models.FloatField(default=0),
        ),
    ]
