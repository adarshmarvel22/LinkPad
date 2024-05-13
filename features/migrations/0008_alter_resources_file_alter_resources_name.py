# Generated by Django 4.1.4 on 2024-05-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_job_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='file',
            field=models.FileField(blank=True, upload_to='resources/'),
        ),
        migrations.AlterField(
            model_name='resources',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
