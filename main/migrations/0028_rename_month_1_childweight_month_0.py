# Generated by Django 5.0.6 on 2024-07-02 20:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0027_rename_user_appointment_patient_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="childweight",
            old_name="month_1",
            new_name="month_0",
        ),
    ]
