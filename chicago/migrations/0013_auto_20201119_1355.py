# Generated by Django 3.1.3 on 2020-11-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicago', '0012_auto_20201119_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_requestsgeneralinfo',
            name='completion_date',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='add_requestsgeneralinfo',
            name='creation_date',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='add_requestsgeneralinfo',
            name='service_request_number',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='add_requestsgeneralinfo',
            name='status',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
