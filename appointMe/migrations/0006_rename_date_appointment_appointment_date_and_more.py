# Generated by Django 4.1.7 on 2023-03-30 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointMe", "0005_appointment_created"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointment", old_name="date", new_name="Appointment_date",
        ),
        migrations.RenameField(
            model_name="appointment", old_name="created", new_name="date_booked",
        ),
    ]
