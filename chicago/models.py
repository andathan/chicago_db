# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class ZipCode(models.Model):
    zipcode = models.CharField(max_length=120)

class Street (models.Model):
    street = models.CharField(max_length=120)


class Query1(models.Model):
    date1 = models.CharField(max_length=120)
    date2 = models.CharField(max_length=120)

class Query2(models.Model):
    date1 = models.CharField(max_length=120)
    date2 = models.CharField(max_length=120)
    request_type =  models.CharField(max_length=120)

class Query3(models.Model):
    date1 = models.CharField(max_length=120)
    
class Query4(models.Model):
    date1 = models.CharField(max_length=120)
    date2 = models.CharField(max_length=120)

class Query5(models.Model):
    date1 = models.CharField(max_length=120)
    x1 = models.CharField(max_length=120)
    x2 = models.CharField(max_length=120)
    y1 = models.CharField(max_length=120)
    y2 = models.CharField(max_length=120)

class Query6(models.Model):
    date1 = models.CharField(max_length=120)
    date2 = models.CharField(max_length=120)

class Query9(models.Model):
    number = models.CharField(max_length=120)

class Query10(models.Model):
    number = models.CharField(max_length=120)

class Query11(models.Model):
    number = models.CharField(max_length=120)

incidents_types = [
    ('Abandoned Vehicle Complaint', 'Abandoned Vehicle Complaint'),
    ('Garbage Cart Black Maintenance/Replacement','Garbage Cart Black Maintenance/Replacement'),
    ('Graffiti Removal','Graffiti Removal'),
    ('Pot Hole in Street','Pot Hole in Street'),
    ('Rodent Baiting/Rat Complaint','Rodent Baiting/Rat Complaint'),
    ('Sanitation Code Violation','Sanitation Code Violation'),
    ('Street Light Out','Street Light Out'),
    ('Street Lights - All/Out','Street Lights - All/Out'),
    ('Tree Debris','Tree Debris'),
    ('Tree Trim','Tree Trim'),
    ('Vacant/Abandoned Building','Vacant/Abandoned Building'),
    ('Alley Light Out','Alley Light Out')
]


class Add_RequestsGeneralInfo(models.Model):
    request_id = models.CharField(max_length=120,blank = True, default = "")
    creation_date = models.CharField(max_length=120,blank = True, default = "")
    status = models.CharField(max_length=120, blank = True, default = "")
    completion_date = models.CharField(max_length=120, blank = True, default = "")
    service_request_number = models.CharField(max_length=120, blank = True, default = "")
    type_of_service_request = models.CharField(max_length=120, choices = incidents_types)


class Add_RequestsGeo(models.Model):
    street_address = models.CharField(max_length=120,blank = True, default = "")
    zip_code = models.CharField(max_length=120,blank = True, default = "")
    wards = models.CharField(max_length=120,blank = True, default = "")
    police_district = models.CharField(max_length=120,blank = True, default = "")
    community_area =models.CharField(max_length=120,blank = True, default = "")
    latitude = models.CharField(max_length=120,blank = True, default = "")
    longitude = models.CharField(max_length=120,blank = True, default = "")
    historical_wards = models.CharField(max_length=120,blank = True, default = "")
    zip_codes = models.CharField(max_length=120,blank = True, default = "")
    community_areas =models.CharField(max_length=120,blank = True, default = "")
    census_tracts = models.CharField(max_length=120,blank = True, default = "")
    ward = models.CharField(max_length=120,blank = True, default = "")
    ssa = models.CharField(max_length=120,blank = True, default = "")
    y_coordinate = models.CharField(max_length=120,blank = True, default = "")
    x_coordinate = models.CharField(max_length=120,blank = True, default = "")
    req_location = models.CharField(max_length=120,blank = True, default = "")


class Add_AbandodedBuildings(models.Model):
    location_of_building = models.CharField(max_length=400, blank=True, null=True)
    building_hazardous = models.CharField(max_length=400, blank=True, null=True)
    building_open = models.CharField(max_length=400, blank=True, null=True)
    entry_point = models.CharField(max_length=400, blank=True, null=True)
    vacant_occupied = models.CharField(max_length=400, blank=True, null=True)
    vacant_due_to_fire = models.CharField(max_length=400, blank=True, null=True)
    people_using_property = models.CharField(max_length=400, blank=True, null=True)



class Add_AbandonedVehicles(models.Model):
    license_plate = models.CharField(max_length=500, blank=True,default = "")
    vehicle_model = models.CharField(max_length=160, blank=True,default = "")
    vehicle_color = models.CharField(max_length=60, blank=True,  default = "")
    current_activity = models.CharField(max_length=500, blank=True, default = "")
    most_recent_action = models.CharField(max_length=500, blank=True, default = "")
    days_reported_parked = models.CharField(max_length=400, blank=True, default = "")


class Add_GarbageCarts(models.Model):
    number_of_black_carts_delivered =  models.CharField(max_length=30, blank=True,default = "")
    current_activity =  models.CharField(max_length=200, blank=True,default = "")
    recent_action = models.CharField(max_length=200, blank=True,default = "")

class Add_GraffitiRemoval(models.Model):
    type_of_surface = models.CharField(max_length=200, blank=True,default = "")
    where_is_located =models.CharField(max_length=200, blank=True,default = "")

class Add_PotHoles(models.Model):
    current_activity = models.CharField(max_length=200, blank=True,default = "")
    recent_action = models.CharField(max_length=200, blank=True,default = "")
    number_of_potholes_filled_on_block = models.CharField(max_length=30, blank=True,default = "")


class Add_RodentBaiting(models.Model):
    number_of_premises_baited = models.CharField(max_length=200, blank=True,default = "")
    number_of_premises_with_garbage =  models.CharField(max_length=200, blank=True,default = "")
    number_of_premises_with_rats =  models.CharField(max_length=200, blank=True,default = "")
    current_activity =  models.CharField(max_length=200, blank=True,default = "")
    recent_action =  models.CharField(max_length=200, blank=True,default = "")

class Add_SanitationCodeComplaints(models.Model):
    nature_of_code_violation =  models.CharField(max_length=200, blank=True,default = "")



class Add_TreeDerbis(models.Model):
    debris_location =models.CharField(max_length=200, blank=True,default = "")
    current_activity = models.CharField(max_length=200, blank=True,default = "")
    most_recent_action =models.CharField(max_length=200, blank=True,default = "")


class Add_TreeTrims(models.Model):
    trees_location = models.CharField(max_length=200, blank=True,default = "")



class AbandodedBuildings(models.Model):
    request = models.OneToOneField('RequestsGeneralInfo', models.DO_NOTHING, primary_key=True)
    location_of_building = models.CharField(max_length=400, blank=True, null=True)
    building_hazardous = models.CharField(max_length=400, blank=True, null=True)
    building_open = models.CharField(max_length=400, blank=True, null=True)
    entry_point = models.CharField(max_length=400, blank=True, null=True)
    vacant_occupied = models.CharField(max_length=400, blank=True, null=True)
    vacant_due_to_fire = models.CharField(max_length=400, blank=True, null=True)
    people_using_property = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abandoded_buildings'


class AbandonedVehicles(models.Model):
    request = models.OneToOneField('RequestsGeneralInfo', models.DO_NOTHING, primary_key=True)
    license_plate = models.CharField(max_length=500, blank=True, null=True)
    vehicle_model = models.CharField(max_length=160, blank=True, null=True)
    vehicle_color = models.CharField(max_length=60, blank=True, null=True)
    current_activity = models.CharField(max_length=500, blank=True, null=True)
    most_recent_action = models.CharField(max_length=500, blank=True, null=True)
    days_reported_parked = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abandoned_vehicles'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GarbageCarts(models.Model):
    request = models.OneToOneField('RequestsGeneralInfo', models.DO_NOTHING, primary_key=True)
    number_of_black_carts_delivered = models.FloatField(blank=True, null=True)
    current_activity = models.CharField(max_length=200, blank=True, null=True)
    recent_action = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garbage_carts'


class GraffitiRemoval(models.Model):
    request = models.OneToOneField('RequestsGeneralInfo', models.DO_NOTHING, primary_key=True)
    type_of_surface = models.CharField(max_length=60, blank=True, null=True)
    where_is_located = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'graffiti_removal'


class PotHoles(models.Model):
    request = models.OneToOneField('RequestsGeneralInfo', models.DO_NOTHING, primary_key=True)
    current_activity = models.CharField(max_length=200, blank=True, null=True)
    recent_action = models.CharField(max_length=200, blank=True, null=True)
    number_of_potholes_filled_on_block = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pot_holes'


class RequestsGeneralInfo(models.Model):
    request_id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(db_column='Creation Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=40, blank=True, null=True)  # Field name made lowercase.
    completion_date = models.DateTimeField(db_column='Completion Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_request_number = models.CharField(db_column='Service Request Number', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_of_service_request = models.CharField(db_column='Type of Service Request', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'requests_general_info'


class RequestsGeo(models.Model):
    request = models.OneToOneField(RequestsGeneralInfo, models.DO_NOTHING, primary_key=True)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    wards = models.FloatField(blank=True, null=True)
    police_district = models.FloatField(blank=True, null=True)
    community_area = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    historical_wards = models.FloatField(blank=True, null=True)
    zip_codes = models.FloatField(blank=True, null=True)
    community_areas = models.FloatField(blank=True, null=True)
    census_tracts = models.FloatField(blank=True, null=True)
    ward = models.FloatField(blank=True, null=True)
    ssa = models.FloatField(blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x_coordinate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    req_location = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests_geo'


class RodentBaiting(models.Model):
    request = models.OneToOneField(RequestsGeneralInfo, models.DO_NOTHING, primary_key=True)
    number_of_premises_baited = models.FloatField(blank=True, null=True)
    number_of_premises_with_garbage = models.FloatField(blank=True, null=True)
    number_of_premises_with_rats = models.FloatField(blank=True, null=True)
    current_activity = models.CharField(max_length=200, blank=True, null=True)
    recent_action = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rodent_baiting'


class SanitationCodeComplaints(models.Model):
    request = models.OneToOneField(RequestsGeneralInfo, models.DO_NOTHING, primary_key=True)
    nature_of_code_violation = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sanitation_code_complaints'


class TreeDerbis(models.Model):
    request = models.OneToOneField(RequestsGeneralInfo, models.DO_NOTHING, primary_key=True)
    debris_location = models.CharField(max_length=200, blank=True, null=True)
    current_activity = models.CharField(max_length=200, blank=True, null=True)
    most_recent_action = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_derbis'


class TreeTrims(models.Model):
    request = models.OneToOneField(RequestsGeneralInfo, models.DO_NOTHING, primary_key=True)
    trees_location = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_trims'
