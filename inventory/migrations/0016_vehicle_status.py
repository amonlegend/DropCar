# Generated by Django 5.0.2 on 2024-04-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_alter_vehicle_road_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('booked', 'booked')], default='available', max_length=100),
        ),
    ]
