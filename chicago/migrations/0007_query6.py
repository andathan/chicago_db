# Generated by Django 3.1.3 on 2020-11-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicago', '0006_query5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.CharField(max_length=120)),
                ('date2', models.CharField(max_length=120)),
            ],
        ),
    ]
