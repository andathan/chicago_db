# Generated by Django 3.1.3 on 2020-11-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicago', '0021_add_treederbis_add_treetrims'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_requestsgeneralinfo',
            name='type_of_service_request',
            field=models.CharField(choices=[('Abandoned Vehicle Complaint', 'Abandoned Vehicle Complaint'), ('Garbage Cart Black Maintenance/Replacement', 'Garbage Cart Black Maintenance/Replacement'), ('Graffiti Removal', 'Graffiti Removal'), ('Pot Hole in Street', 'Pot Hole in Street'), ('Rodent Baiting/Rat Complaint', 'Rodent Baiting/Rat Complaint'), ('Sanitation Code Violation', 'Sanitation Code Violation'), ('Street Light Out', 'Street Light Out'), ('Street Lights - All/Out', 'Street Lights - All/Out'), ('Tree Debris', 'Tree Debris'), ('Tree Trim', 'Tree Trim'), ('Vacant/Abandoned Building', 'Vacant/Abandoned Building'), ('Alley Light Out', 'Alley Light Out')], max_length=120),
        ),
    ]
