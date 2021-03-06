# Generated by Django 3.1.3 on 2020-11-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicago', '0020_auto_20201119_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_TreeDerbis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debris_location', models.CharField(blank=True, default='', max_length=200)),
                ('current_activity', models.CharField(blank=True, default='', max_length=200)),
                ('most_recent_action', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Add_TreeTrims',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trees_location', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
    ]
