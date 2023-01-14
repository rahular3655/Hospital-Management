# Generated by Django 4.1.4 on 2023-01-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_remove_patients_doctor_patients_doctors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalconditions',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='medical_condition',
        ),
        migrations.AddField(
            model_name='patients',
            name='medical_condition',
            field=models.ManyToManyField(max_length=1000, to='patients.medicalconditions'),
        ),
    ]
