# Generated by Django 5.0.6 on 2024-05-11 16:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("features", "0005_alter_job_added_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="added_by",
        ),
    ]
