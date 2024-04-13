# Generated by Django 5.0.2 on 2024-04-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_remove_roadtype_vehicles_alter_roadtype_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='price',
            new_name='price_per_day',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='recommended_places',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_number',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
