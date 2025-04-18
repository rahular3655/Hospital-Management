# Generated by Django 5.2 on 2025-04-18 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('common', '0003_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='blood_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profiles', to='common.bloodgroup'),
        ),
    ]
