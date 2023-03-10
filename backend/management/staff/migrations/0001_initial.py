# Generated by Django 4.1.4 on 2022-12-21 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/Attenders')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('specialized_in', models.CharField(max_length=150, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('status', models.CharField(choices=[('new', 'new'), ('Senior', 'Senior'), ('Experienced', 'Experienced')], default='new', max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/Doctors')),
            ],
        ),
        migrations.CreateModel(
            name='Helpers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/Helpers')),
            ],
        ),
        migrations.CreateModel(
            name='Labassistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/Labassistant')),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/Managers')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('status', models.CharField(choices=[('new', 'new'), ('Senior', 'Senior'), ('HeadNurse', 'HeadNurse')], default='new', max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/Nurse')),
            ],
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('designation', models.CharField(max_length=150, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/others')),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/Receptionist')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_join', models.DateField()),
                ('phonenumber', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=5, null=True)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/Security')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attenders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.attenders')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.doctor')),
                ('helpers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.helpers')),
                ('labassistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.labassistant')),
                ('managers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.managers')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.nurse')),
                ('others', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.others')),
                ('receptionist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.receptionist')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.security')),
            ],
        ),
    ]
