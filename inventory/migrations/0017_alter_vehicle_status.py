# Generated by Django 5.0.2 on 2024-04-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_vehicle_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('booked', 'Booked')], default='available', max_length=100),
        ),
    ]
