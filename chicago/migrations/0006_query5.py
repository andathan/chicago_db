# Generated by Django 3.1.3 on 2020-11-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicago', '0005_query4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(max_length=120)),
                ('x1', models.CharField(max_length=120)),
                ('x2', models.CharField(max_length=120)),
                ('y1', models.CharField(max_length=120)),
                ('y2', models.CharField(max_length=120)),
            ],
        ),
    ]
