# Generated by Django 5.0.2 on 2024-05-17 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_alter_vehicle_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pickup_date', models.DateTimeField()),
                ('drop_off_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('booked', 'Booked'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
