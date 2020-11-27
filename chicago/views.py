from django.shortcuts import render,redirect
from django.http import HttpResponse
from chicago.models import *
from django.db import connection
from .forms import *
import string

# Create your views here.

def add_quotes_or_null(input_string):
  input_string = str(input_string)
  if not input_string:
      input_string = "null"
  else:
      input_string = "'" + input_string + "'"
  return input_string

def home_view(request,*args, **kwargs):
      return render(request,"home.html",{})



def search_zip_code_form(request):
  form = ZipCodeForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = ZipCodeForm()
    return redirect('search_zip_code.html') 
  context = {
            'form' :form
      }
  return render(request,"search_zip_code_form.html",context)


def search_zip_code(request):
    zipcode = ZipCode.objects.last().zipcode
    raw_query = "SELECT * \
from requests_general_info natural join requests_geo \
WHERE zip_code_float = " + zipcode + " \
    "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
      }
    return render(request,"search_zip_code.html",context)




def search_street_form(request):
  form = StreetForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = StreetForm()
    return redirect('search_street.html') 
  context = {
            'form' :form
      }
  return render(request,"search_street_form.html",context)



#TO_DO::
def search_street(request):
    street = Street.objects.last().street
    raw_query = "SELECT * \
from requests_general_info natural join requests_geo \
WHERE street_address = '" + street + "' \
    "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
      }
    return render(request,"search_street.html",context)





def add_tree_debris_form(request):
  form = Add_TreeDerbisForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_TreeDerbisForm()
    return redirect('add_tree_debris.html') 
  context = {
            'form' :form
      }
  return render(request,"add_tree_debris_form.html",context)

def add_tree_debris(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  debris_location = add_quotes_or_null(Add_TreeDerbis.objects.last().debris_location)
  current_activity = add_quotes_or_null(Add_TreeDerbis.objects.last().current_activity)
  most_recent_action = add_quotes_or_null(Add_TreeDerbis.objects.last().most_recent_action)


  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      debris_location,
      current_activity,
      most_recent_action
    ]

  to_add = ','.join(fields)
  raw_query = " INSERT INTO tree_derbis \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")




def add_tree_trim_form(request):
  form = Add_TreeTrimsForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_TreeTrimsForm()
    return redirect('add_tree_trim.html') 
  context = {
            'form' :form
      }
  return render(request,"add_tree_trim_form.html",context)


def add_tree_trim(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  trees_location = add_quotes_or_null(Add_TreeTrims.objects.last().trees_location)


  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      trees_location
    ]

  to_add = ','.join(fields)
  raw_query = " INSERT INTO tree_trims \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")


def add_rodent_bait(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  number_of_premises_baited = add_quotes_or_null(Add_RodentBaiting.objects.last().number_of_premises_baited)
  number_of_premises_with_garbage = add_quotes_or_null(Add_RodentBaiting.objects.last().number_of_premises_with_garbage)
  number_of_premises_with_rats = add_quotes_or_null(Add_RodentBaiting.objects.last().number_of_premises_with_rats)
  current_activity = add_quotes_or_null(Add_RodentBaiting.objects.last().current_activity)
  recent_action = add_quotes_or_null(Add_RodentBaiting.objects.last().recent_action)

  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      number_of_premises_baited,
      number_of_premises_with_garbage,
      number_of_premises_with_rats,
      current_activity,
      recent_action
    ]

  to_add = ','.join(fields)
  raw_query = " INSERT INTO rodent_baiting \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")







def add_rodent_bait_form(request):
  form = Add_RodentBaitingForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_RodentBaitingForm()
    return redirect('add_rodent_bait.html') 
  context = {
            'form' :form
      }
  return render(request,"add_rodent_bait_form.html",context)



def add_rodent_bait(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  number_of_premises_baited = add_quotes_or_null(Add_RodentBaiting.objects.last().number_of_premises_baited)
  number_of_premises_with_garbage = add_quotes_or_null(Add_RodentBaiting.objects.last().number_of_premises_with_garbage)
  number_of_premises_with_rats = add_quotes_or_null(Add_RodentBaiting.objects.last().number_of_premises_with_rats)
  current_activity = add_quotes_or_null(Add_RodentBaiting.objects.last().current_activity)
  recent_action = add_quotes_or_null(Add_RodentBaiting.objects.last().recent_action)

  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      number_of_premises_baited,
      number_of_premises_with_garbage,
      number_of_premises_with_rats,
      current_activity,
      recent_action
    ]

  to_add = ','.join(fields)
  raw_query = " INSERT INTO rodent_baiting \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")





def add_sanitation_code_form(request):
  form = Add_SanitationCodeComplaintsForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_SanitationCodeComplaintsForm()
    return redirect('add_sanitation_code.html') 
  context = {
            'form' :form
      }
  return render(request,"add_sanitation_code_form.html",context)


def add_sanitation_code(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  nature_of_code_violation = add_quotes_or_null(Add_SanitationCodeComplaints.objects.last().nature_of_code_violation)

  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      nature_of_code_violation
    ]
  to_add = ','.join(fields)
  raw_query = " INSERT INTO sanitation_code_complaints \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")








def add_graffiti_removal_form(request):
  form = Add_GraffitiRemovalForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_GraffitiRemovalForm()
    return redirect('add_graffiti_removal.html') 
  context = {
            'form' :form
      }
  return render(request,"add_graffiti_removal_form.html",context)




def add_graffiti_removal(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  type_of_surface = add_quotes_or_null(Add_GraffitiRemoval.objects.last().type_of_surface)
  where_is_located = add_quotes_or_null(Add_GraffitiRemoval.objects.last().where_is_located)

  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      type_of_surface,
      where_is_located
    ]
  to_add = ','.join(fields)
  raw_query = " INSERT INTO graffiti_removal \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")



def add_potholes_form(request):
  form = Add_PotHolesForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_PotHolesForm()
    return redirect('add_potholes.html') 
  context = {
            'form' :form
      }
  return render(request,"add_potholes_form.html",context)


def add_potholes(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  current_activity = add_quotes_or_null(Add_PotHoles.objects.last().current_activity)
  recent_action = add_quotes_or_null(Add_PotHoles.objects.last().recent_action)
  number_of_potholes_filled_on_block = add_quotes_or_null(Add_PotHoles.objects.last().number_of_potholes_filled_on_block)


  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      current_activity,
      recent_action,
      number_of_potholes_filled_on_block
    ]
  to_add = ','.join(fields)
  raw_query = " INSERT INTO pot_holes \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")




def add_garbage_carts_form(request):
  form = Add_GarbageCartsForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_GarbageCartsForm()
    return redirect('add_garbage_carts.html') 
  context = {
            'form' :form
      }
  return render(request,"add_garbage_carts_form.html",context)


def add_garbage_carts(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  number_of_black_carts_delivered = add_quotes_or_null(Add_GarbageCarts.objects.last().number_of_black_carts_delivered)
  current_activity = add_quotes_or_null(Add_GarbageCarts.objects.last().current_activity)
  recent_action =  add_quotes_or_null(Add_GarbageCarts.objects.last().recent_action)

  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      number_of_black_carts_delivered,
      current_activity,
      recent_action
    ]
  to_add = ','.join(fields)
  raw_query = " INSERT INTO garbage_carts \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")



def add_garbage_carts(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  number_of_black_carts_delivered = add_quotes_or_null(Add_GarbageCarts.objects.last().number_of_black_carts_delivered)
  current_activity = add_quotes_or_null(Add_GarbageCarts.objects.last().current_activity)
  recent_action =  add_quotes_or_null(Add_GarbageCarts.objects.last().recent_action)

  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      number_of_black_carts_delivered,
      current_activity,
      recent_action
    ]
  to_add = ','.join(fields)
  raw_query = " INSERT INTO garbage_carts \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")


def add_abandoned_vehicle_form(request):
  form = Add_AbandonedVehiclesForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_AbandonedVehiclesForm()
    return redirect('add_abandoned_vehicle.html') 
  context = {
            'form' :form
      }
  return render(request,"add_abandoned_vehicle_form.html",context)



def add_abandoned_vehicle(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  license_plate = add_quotes_or_null(Add_AbandonedVehicles.objects.last().license_plate)
  vehicle_model = add_quotes_or_null(Add_AbandonedVehicles.objects.last().vehicle_model)
  vehicle_color =  add_quotes_or_null(Add_AbandonedVehicles.objects.last().vehicle_color)
  current_activity = add_quotes_or_null(Add_AbandonedVehicles.objects.last().current_activity)
  most_recent_action = add_quotes_or_null(Add_AbandonedVehicles.objects.last().most_recent_action)
  days_reported_parked = add_quotes_or_null(Add_AbandonedVehicles.objects.last().days_reported_parked)
  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      license_plate,
      vehicle_model,
      vehicle_color,
      current_activity,
      most_recent_action,
      days_reported_parked
    ]
  to_add = ','.join(fields)
  raw_query = " INSERT INTO abandoned_vehicles \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")

def add_vacant_building_form(request):
  form = Add_AbandodedBuildingsForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = Add_AbandodedBuildingsForm()
    return redirect('add_vacant_building.html') 
  context = {
            'form' :form
      }
  return render(request,"add_vacant_building_form.html",context)

def add_vacant_building(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  location_of_building = add_quotes_or_null(Add_AbandodedBuildings.objects.last().location_of_building)
  building_hazardous = add_quotes_or_null(Add_AbandodedBuildings.objects.last().building_hazardous)
  building_open =  add_quotes_or_null(Add_AbandodedBuildings.objects.last().building_open)
  vacant_occupied = add_quotes_or_null(Add_AbandodedBuildings.objects.last().vacant_occupied)
  vacant_due_to_fire = add_quotes_or_null(Add_AbandodedBuildings.objects.last().vacant_due_to_fire)
  people_using_property = add_quotes_or_null(Add_AbandodedBuildings.objects.last().people_using_property)
  entry_point = add_quotes_or_null(Add_AbandodedBuildings.objects.last().entry_point)
  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )
  fields = [
      request_id,
      location_of_building,
      building_hazardous,
      building_open,
      entry_point,
      vacant_occupied,
      vacant_due_to_fire,
      people_using_property
    ]

  to_add = ','.join(fields)
  raw_query = " INSERT INTO abandoded_buildings \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  return redirect("done.html")


def add_geo_form_view(request):
  form = AddGeoForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = AddGeoForm()
    return redirect('add_geo.html') 
  context = {
            'form' :form
      }
  return render(request,"add_geo_form.html",context)


def add_geo_view(request):
  request_id = Add_RequestsGeneralInfo.objects.last().request_id
  #read input from form
  #add single quotes when not null. add "null" string when var is empty
  street_address = add_quotes_or_null(Add_RequestsGeo.objects.last().street_address)
  zip_code = add_quotes_or_null(Add_RequestsGeo.objects.last().zip_code)
  wards =  add_quotes_or_null(Add_RequestsGeo.objects.last().wards)
  police_district = add_quotes_or_null(Add_RequestsGeo.objects.last().police_district)
  community_area = add_quotes_or_null(Add_RequestsGeo.objects.last().community_area)
  latitude = add_quotes_or_null(Add_RequestsGeo.objects.last().latitude)
  longitude = add_quotes_or_null(Add_RequestsGeo.objects.last().longitude)
  zip_codes = add_quotes_or_null(Add_RequestsGeo.objects.last().zip_codes)
  historical_wards = add_quotes_or_null(Add_RequestsGeo.objects.last().historical_wards)
  community_areas = add_quotes_or_null(Add_RequestsGeo.objects.last().community_areas)
  census_tracts = add_quotes_or_null(Add_RequestsGeo.objects.last().census_tracts)
  ward = add_quotes_or_null(Add_RequestsGeo.objects.last().ward)
  y_coordinate = add_quotes_or_null(Add_RequestsGeo.objects.last().y_coordinate)
  x_coordinate = add_quotes_or_null(Add_RequestsGeo.objects.last().x_coordinate)
  req_location = add_quotes_or_null(Add_RequestsGeo.objects.last().req_location)
  ssa = add_quotes_or_null(Add_RequestsGeo.objects.last().ssa)

  #if no zip code provided
  zip_code_float = "null"
  if zip_code != "null":
    zip_code_float = "" + Add_RequestsGeo.objects.last().zip_code + ".0"

  #req_location should have quotes so we need to espace them
  if req_location != "null":
    req_location = "'"+ req_location[1:-1].replace("'", "") + "' "

  if not request_id:
      request_id = str(RequestsGeneralInfo.objects.last().request_id )

  fields = [
      request_id,
      street_address,
      zip_code,
      wards,
      police_district,
      community_area,
      latitude,
      longitude,
      historical_wards,
      zip_codes,
      community_areas,
      census_tracts,
      ward,
      ssa,
      y_coordinate,
      x_coordinate,
      req_location,
      zip_code_float
    ]
  to_add = ','.join(fields)
  raw_query = " INSERT INTO requests_geo \
  VALUES (" + to_add + ")"
  cursor = connection.cursor()
  cursor.execute(raw_query)
  context = {
            'request_id' :request_id
      }
  incident_choosen =  Add_RequestsGeneralInfo.objects.last().type_of_service_request
  if (incident_choosen == "Abandoned Vehicle Complaint"):
    next_page = "add_abandoned_vehicle_form.html"
  elif (incident_choosen == "Garbage Cart Black Maintenance/Replacement"):
    next_page = "add_garbage_carts_form.html"
  elif (incident_choosen == "Graffiti Removal"):
    next_page = "add_graffiti_removal_form.html"    
  elif (incident_choosen == "Pot Hole in Street"):
    next_page = "add_potholes_form.html"    
  elif (incident_choosen == "Rodent Baiting/Rat Complaint"):
    next_page = "add_rodent_bait_form.html"    
  elif (incident_choosen == "Sanitation Code Violation"):
    next_page = "add_sanitation_code_form.html"    
  elif (incident_choosen == "Street Light Out"):
    next_page = "done.html"    
  elif (incident_choosen == "Alley Light Out"):
    next_page = "done.html" 
  elif (incident_choosen == "'Street Lights - All/Out'"):
    next_page = "done.html"    
  elif (incident_choosen == "Tree Debris"):
    next_page = "add_tree_debris_form.html"    
  elif (incident_choosen == "Tree Trim"):
    next_page = "add_tree_trim_form.html"    
  elif (incident_choosen == "Vacant/Abandoned Building"):
    next_page = "add_vacant_building_form.html"    
  else:
    next_page = "done.html"
  return redirect(next_page)
  #return render(request,"add_geo.html",context)

def add_form_view(request):
  form = AddGeneralForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = AddGeneralForm()
    return redirect('add.html') 
  context = {
            'form' :form
      }
  return render(request,"add_form.html",context)

def add_view(request):
    request_id = Add_RequestsGeneralInfo.objects.last().request_id
    creation_date = Add_RequestsGeneralInfo.objects.last().creation_date
    status = Add_RequestsGeneralInfo.objects.last().status
    completion_date =  Add_RequestsGeneralInfo.objects.last().completion_date
    service_request_number = Add_RequestsGeneralInfo.objects.last().service_request_number
    type_of_service_request=  Add_RequestsGeneralInfo.objects.last().type_of_service_request
    #add single quotes when not null. add "null" string when var is empty
    if not request_id:
      request_id = RequestsGeneralInfo.objects.last().request_id + 1 
    if not creation_date:
      creation_date = "null"
    else:
      creation_date = "'" + creation_date + "'"
    if not status:
      status = "null"
    else:
      status = "'" + status + "'"
    if not completion_date:
      completion_date = "null"
    else:
      completion_date = "'" + completion_date + "'"
    if not service_request_number:
      service_request_number = "null"
    else:
      service_request_number = "'" + service_request_number + "'"
  

    to_add = str(request_id) + ", " + str(creation_date) + "," + status + "," + str(completion_date) + "," +service_request_number + ", '" + type_of_service_request + "'"
    raw_query = " INSERT INTO requests_general_info \
VALUES (" + to_add + ")"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    context = {
            'request_id' :request_id
      }
    return redirect('add_geo_form.html') 
    #return render(request,"add.html",context)



def done_view(request):
  request_id = RequestsGeneralInfo.objects.last().request_id
  type_of_service_request = Add_RequestsGeneralInfo.objects.last().type_of_service_request
  context = {
            'request_id' :request_id,
            'type_of_service_request' : type_of_service_request,
      }
  return render(request,"done.html",context)
def query1_view(request):
    start_date = Query1.objects.last().date1
    end_date = Query1.objects.last().date2
    raw_query = "SELECT \"Type of Service Request\", COUNT(*) as \"Number\" FROM requests_general_info WHERE \"Creation Date\" > \'" + start_date + "\' AND \"Creation Date\" < \'" + end_date+ "\' GROUP BY \"Type of Service Request\" ORDER BY \"Number\" desc"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'start_date' : start_date,
            'end_date' : end_date
      }
    return render(request,"query1.html",context)




def query1_form_view(request):
	form = Query1Form(request.POST or None)
	if form.is_valid():
		form.save()
		form = Query1Form()
		return redirect('query1.html') 
	context = {
            'form' :form
      }
	return render(request,"query1_form.html",context)
def query1_view(request):
    start_date = Query1.objects.last().date1
    end_date = Query1.objects.last().date2
    raw_query = "SELECT \"Type of Service Request\", COUNT(*) as \"Number\" FROM requests_general_info WHERE \"Creation Date\" > \'" + start_date + "\' AND \"Creation Date\" < \'" + end_date+ "\' GROUP BY \"Type of Service Request\" ORDER BY \"Number\" desc"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'start_date' : start_date,
            'end_date' : end_date
      }
    return render(request,"query1.html",context)



def query2_form_view(request):
	form = Query2Form(request.POST or None)
	if form.is_valid():
		form.save()
		form = Query2Form()
		return redirect('query2.html') 
	context = {
            'form' :form
      }
	return render(request,"query2_form.html",context)
def query2_view(request):
    start_date = Query2.objects.last().date1
    end_date = Query2.objects.last().date2
    request_type = Query2.objects.last().request_type
    raw_query = "SELECT \"Creation Date\", COUNT(*) FROM requests_general_info WHERE \"Creation Date\" > '" + start_date + "' AND \"Creation Date\" < '" + end_date + "'AND \"Type of Service Request\" = '" +  request_type +  "'GROUP BY \"Creation Date\" ORDER BY \"Creation Date\""
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'start_date' : start_date,
            'end_date' : end_date,
            'request_type' : request_type
      }
    return render(request,"query2.html",context)

def query3_form_view(request):
	form = Query3Form(request.POST or None)
	if form.is_valid():
		form.save()
		form = Query3Form()
		return redirect('query3.html') 
	context = {
            'form' :form
      }
	return render(request,"query3_form.html",context)

def query3_view(request):
    start_date = Query3.objects.last().date1
    raw_query = "SELECT zip_code, \"Type of Service Request\" FROM (SELECT zip_code, \"Type of Service Request\", rank() OVER (PARTITION BY zip_code ORDER BY COUNT(\"Type of Service Request\") DESC)  FROM requests_general_info natural join requests_geo WHERE \"Creation Date\" = '" + start_date + "' and zip_code is not null and zip_code != '0.0' GROUP BY zip_code,\"Type of Service Request\") ranked_zip_codes where rank <=1"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'start_date' : start_date
      }
    return render(request,"query3.html",context)

def query4_form_view(request):
	form = Query4Form(request.POST or None)
	if form.is_valid():
		form.save()
		form = Query4Form()
		return redirect('query4.html') 
	context = {
            'form' :form
      }
	return render(request,"query4_form.html",context)
def query4_view(request):
    start_date = Query4.objects.last().date1
    end_date = Query4.objects.last().date2
    raw_query = "SELECT \"Type of Service Request\", AVG(\"Completion Date\" - \"Creation Date\") FROM requests_general_info WHERE \"Creation Date\" >'"+ start_date + "' AND \"Creation Date\" < '" + end_date + "' GROUP BY \"Type of Service Request\""
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'start_date' : start_date,
            'end_date' : end_date
      }
    return render(request,"query4.html",context)

def query5_form_view(request):
	form = Query5Form(request.POST or None)
	if form.is_valid():
		form.save()
		form = Query5Form()
		return redirect('query5.html') 
	context = {
            'form' :form
      }
	return render(request,"query5_form.html",context)
def query5_view(request):
    start_date = Query5.objects.last().date1
    x1  = Query5.objects.last().x1
    x2 = Query5.objects.last().x2
    y1 = Query5.objects.last().y1
    y2 = Query5.objects.last().y2
    raw_query = "SELECT \"Type of Service Request\", COUNT(*)\
FROM requests_general_info natural join requests_geo \
  WHERE \"Creation Date\" = '" + start_date+ "' \
  AND \"latitude\" > " + x1 + "\
  AND \"longitude\" > " + y1 + "\
  AND \"latitude\" < " + x2 + "\
  AND \"longitude\" > " + y1 + "\
  AND \"latitude\" > " + x1 + "\
  AND \"longitude\" < " + y2 + "\
   AND \"latitude\" <" + x2 + "\
  AND \"longitude\" <" + y2 + " GROUP BY \"Type of Service Request\" \
  ORDER BY count desc\
  LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'start_date': start_date,
            'x1' : x1,
            'y1' : y1,
            'x2' : x2,
            'y2' : y2
      }
    return render(request,"query5.html",context)

def query6_form_view(request):
	form = Query6Form(request.POST or None)
	if form.is_valid():
		form.save()
		form = Query6Form()
		return redirect('query6.html') 
	context = {
            'form' :form
      }
	return render(request,"query6_form.html",context)
def query6_view(request):
    start_date = Query6.objects.last().date1
    end_date = Query6.objects.last().date2
    raw_query = " SELECT \"ssa\", COUNT(*) \
FROM requests_general_info natural join requests_geo \
WHERE \"Creation Date\" >'" + start_date + "' AND \"Creation Date\" < '" + end_date + "'\
AND \"ssa\" != -1\
GROUP BY \"ssa\"\
ORDER BY count desc \
LIMIT 5"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'start_date' : start_date,
            'end_date' : end_date
      }
    return render(request,"query6.html",context)


def query7_view(request):
    raw_query = "SELECT license_plate, count_times \
FROM (\
SELECT license_plate, COUNT(*) as count_times \
FROM abandoned_vehicles \
WHERE license_plate NOT LIKE '-%' \
AND license_plate NOT LIKE '?%' \
AND license_plate NOT LIKE '(%' \
AND license_plate NOT LIKE ',%' \
AND license_plate NOT LIKE '.%' \
AND license_plate IS NOT null \
GROUP BY license_plate) grouped_licenses_plated \
WHERE count_times >1"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
      }
    return render(request,"query7.html",context)

def query8_view(request):
    raw_query = "SELECT vehicle_color,COUNT(*) \
FROM abandoned_vehicles \
GROUP BY vehicle_color \
order by count desc \
OFFSET 1 \
LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
      }
    return render(request,"query8.html",context)

def query9_form_view(request):
  form = Query9Form(request.POST or None)
  if form.is_valid():
    form.save()
    form = Query9Form()
    return redirect('query9.html') 
  context = {
            'form' :form
      }
  return render(request,"query9_form.html",context)
def query9_view(request):
    number = Query9.objects.last().number
    raw_query = "SELECT request_id,  \"number_of_premises_baited\" \
FROM rodent_baiting \
WHERE \"number_of_premises_baited\" is not null and \"number_of_premises_baited\" <" + number + "; "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'number' : number
      }
    return render(request,"query9.html",context)


def query10_form_view(request):
  form = Query10Form(request.POST or None)
  if form.is_valid():
    form.save()
    form = Query10Form()
    return redirect('query10.html') 
  context = {
            'form' :form
      }
  return render(request,"query10_form.html",context)
def query10_view(request):
    number = Query10.objects.last().number
    raw_query = "SELECT request_id,  \"number_of_premises_with_garbage\" \
FROM rodent_baiting \
WHERE \"number_of_premises_with_garbage\" is not null and \"number_of_premises_with_garbage\" <" + number + "; "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'number' : number
      }
    return render(request,"query10.html",context)

def query11_form_view(request):
  form = Query11Form(request.POST or None)
  if form.is_valid():
    form.save()
    form = Query11Form()
    return redirect('query11.html') 
  context = {
            'form' :form
      }
  return render(request,"query11_form.html",context)

def query11_view(request):
    number = Query11.objects.last().number
    raw_query = "SELECT request_id,  \"number_of_premises_with_rats\" \
FROM rodent_baiting \
WHERE \"number_of_premises_with_rats\" is not null and \"number_of_premises_with_rats\" <" + number + "; "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
            'number' : number
      }
    return render(request,"query11.html",context)


def query12_view(request):
    raw_query = "SELECT a.police_district FROM  \
(SELECT police_district ,\"Completion Date\", COUNT (*) \
FROM requests_general_info natural join requests_geo natural join pot_holes \
WHERE police_district IS NOT null \
GROUP BY police_district,\"Completion Date\")  as a \
JOIN \
(SELECT police_district , \"Completion Date\",COUNT (*) \
FROM requests_general_info natural join requests_geo natural join rodent_baiting \
WHERE police_district IS NOT null \
GROUP BY police_district,\"Completion Date\") as b  \
on a.police_district = b.police_district AND a.\"Completion Date\" = b.\"Completion Date\" \
GROUP BY a.police_district "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    obj = cursor.fetchall()
    context = {
            'object' :obj,
      }
    return render(request,"query12.html",context)





