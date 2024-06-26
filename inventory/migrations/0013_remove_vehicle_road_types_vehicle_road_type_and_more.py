# Generated by Django 5.0.2 on 2024-04-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_vehicle_seats_alter_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='road_types',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='Road_Type',
            field=models.CharField(choices=[('Highway', 'Highway'), ('Urban', 'Urban'), ('Rural', 'Rural'), ('Mountain', 'Mountain'), ('Street', 'Street'), ('Off-road', 'Off-road')], default='Highway', max_length=100),
        ),
        migrations.DeleteModel(
            name='RoadType',
        ),
    ]
