# Generated by Django 4.1.4 on 2023-01-21 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_medicalconditions_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='medical_condition',
        ),
    ]
