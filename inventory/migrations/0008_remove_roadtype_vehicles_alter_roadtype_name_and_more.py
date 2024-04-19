# Generated by Django 5.0.2 on 2024-04-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_roadtype_vehicles_remove_roadtype_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roadtype',
            name='vehicles',
        ),
        migrations.AlterField(
            model_name='roadtype',
            name='name',
            field=models.CharField(choices=[('Highway', 'Highway'), ('Urban', 'Urban'), ('Rural', 'Rural'), ('Mountain', 'Mountain'), ('Off-road', 'Off-road')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='road_types',
            field=models.ManyToManyField(blank=True, related_name='vehicle_road_types', to='inventory.roadtype'),
        ),
    ]