# Generated by Django 5.0.4 on 2024-05-06 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_childfirstattendence_childmonitoringattendance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='childfirstattendence',
            name='pregnancy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pregnancy'),
        ),
        migrations.AddField(
            model_name='childmonitoringattendance',
            name='pregnancy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pregnancy'),
        ),
        migrations.AddField(
            model_name='childvaccineinfo',
            name='pregnancy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pregnancy'),
        ),
    ]
