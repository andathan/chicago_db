# Generated by Django 3.1.3 on 2020-11-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicago', '0007_query6'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=120)),
            ],
        ),
    ]
