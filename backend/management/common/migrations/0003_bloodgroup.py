# Generated by Django 5.2 on 2025-04-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, unique=True)),
            ],
        ),
    ]
