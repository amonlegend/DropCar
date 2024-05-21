# Generated by Django 5.0.2 on 2024-05-02 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_booking'),
        ('inventory', '0018_alter_vehicle_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.vehicle'),
            preserve_default=False,
        ),
    ]