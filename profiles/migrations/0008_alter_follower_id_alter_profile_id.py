# Generated by Django 5.0.6 on 2024-05-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0007_auto_20220211_1227"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follower",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]