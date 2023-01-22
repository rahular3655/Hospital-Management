# Generated by Django 4.1.4 on 2023-01-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('Condition', models.CharField(choices=[('Working', 'Working'), ('Repair', 'Repair'), ('Fixed', 'Fixed')], max_length=100, null=True)),
                ('Floor', models.ManyToManyField(null=True, to='infrastructure.floors')),
            ],
        ),
    ]