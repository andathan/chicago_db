# Generated by Django 3.1.3 on 2020-11-14 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RequestsGeneralInfo',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(blank=True, db_column='Creation Date', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=40, null=True)),
                ('completion_date', models.DateTimeField(blank=True, db_column='Completion Date', null=True)),
                ('service_request_number', models.CharField(blank=True, db_column='Service Request Number', max_length=40, null=True)),
                ('type_of_service_request', models.CharField(blank=True, db_column='Type of Service Request', max_length=60, null=True)),
            ],
            options={
                'db_table': 'requests_general_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AbandodedBuildings',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('location_of_building', models.CharField(blank=True, max_length=400, null=True)),
                ('building_hazardous', models.CharField(blank=True, max_length=400, null=True)),
                ('building_open', models.CharField(blank=True, max_length=400, null=True)),
                ('entry_point', models.CharField(blank=True, max_length=400, null=True)),
                ('vacant_occupied', models.CharField(blank=True, max_length=400, null=True)),
                ('vacant_due_to_fire', models.CharField(blank=True, max_length=400, null=True)),
                ('people_using_property', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'abandoded_buildings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AbandonedVehicles',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('license_plate', models.CharField(blank=True, max_length=500, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=160, null=True)),
                ('vehicle_color', models.CharField(blank=True, max_length=60, null=True)),
                ('current_activity', models.CharField(blank=True, max_length=500, null=True)),
                ('most_recent_action', models.CharField(blank=True, max_length=500, null=True)),
                ('days_reported_parked', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'abandoned_vehicles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GarbageCarts',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('number_of_black_carts_delivered', models.FloatField(blank=True, null=True)),
                ('current_activity', models.CharField(blank=True, max_length=200, null=True)),
                ('recent_action', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'garbage_carts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GraffitiRemoval',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('type_of_surface', models.CharField(blank=True, max_length=60, null=True)),
                ('where_is_located', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'graffiti_removal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PotHoles',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('current_activity', models.CharField(blank=True, max_length=200, null=True)),
                ('recent_action', models.CharField(blank=True, max_length=200, null=True)),
                ('number_of_potholes_filled_on_block', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pot_holes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RequestsGeo',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('wards', models.FloatField(blank=True, null=True)),
                ('police_district', models.FloatField(blank=True, null=True)),
                ('community_area', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('historical_wards', models.FloatField(blank=True, null=True)),
                ('zip_codes', models.FloatField(blank=True, null=True)),
                ('community_areas', models.FloatField(blank=True, null=True)),
                ('census_tracts', models.FloatField(blank=True, null=True)),
                ('ward', models.FloatField(blank=True, null=True)),
                ('ssa', models.FloatField(blank=True, null=True)),
                ('y_coordinate', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('x_coordinate', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('req_location', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'requests_geo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RodentBaiting',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('number_of_premises_baited', models.FloatField(blank=True, null=True)),
                ('number_of_premises_with_garbage', models.FloatField(blank=True, null=True)),
                ('number_of_premises_with_rats', models.FloatField(blank=True, null=True)),
                ('current_activity', models.CharField(blank=True, max_length=200, null=True)),
                ('recent_action', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'rodent_baiting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SanitationCodeComplaints',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('nature_of_code_violation', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'sanitation_code_complaints',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreeDerbis',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('debris_location', models.CharField(blank=True, max_length=200, null=True)),
                ('current_activity', models.CharField(blank=True, max_length=200, null=True)),
                ('most_recent_action', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'tree_derbis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreeTrims',
            fields=[
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='chicago.requestsgeneralinfo')),
                ('trees_location', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'tree_trims',
                'managed': False,
            },
        ),
    ]
