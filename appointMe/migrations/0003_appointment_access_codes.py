# Generated by Django 4.1.7 on 2023-03-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointMe", "0002_appointment"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="access_codes",
            field=models.CharField(default=0, max_length=190),
        ),
    ]
