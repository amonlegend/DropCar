# Generated by Django 5.0.2 on 2024-04-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_vehicle_drop_off_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadtype',
            name='vehicles',
            field=models.ManyToManyField(blank=True, related_name='road_type_vehicles', to='inventory.vehicle'),
        ),
        migrations.RemoveField(
            model_name='roadtype',
            name='name',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='road_types',
            field=models.ManyToManyField(blank=True, null=True, related_name='vehicle_road_types', to='inventory.roadtype'),
        ),
        migrations.AddField(
            model_name='roadtype',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]