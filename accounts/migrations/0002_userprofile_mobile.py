# Generated by Django 4.2.6 on 2023-11-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="mobile",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
