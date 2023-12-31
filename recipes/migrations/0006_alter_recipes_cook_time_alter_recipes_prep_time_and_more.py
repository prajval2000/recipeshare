# Generated by Django 4.2.6 on 2023-10-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0005_alter_recipes_nutrition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipes",
            name="cook_time",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="prep_time",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="servings",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="timing",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="total_time",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="yields",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
