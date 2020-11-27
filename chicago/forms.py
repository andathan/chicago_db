from django import forms


from .models import * 


class ZipCodeForm(forms.ModelForm):
	class Meta:
		model = ZipCode
		fields = [
			'zipcode'
		]



class StreetForm(forms.ModelForm):
	class Meta:
		model = Street
		fields = [
			'street'
		]


class Query1Form(forms.ModelForm):
	class Meta:
		model = Query1
		fields = [
			'date1',
			'date2'
		]
class Query2Form(forms.ModelForm):
	class Meta:
		model = Query2
		fields = [
			'date1',
			'date2',
			'request_type'
		]
class Query3Form(forms.ModelForm):
	class Meta:
		model = Query3
		fields = [
			'date1',
		]

class Query4Form(forms.ModelForm):
	class Meta:
		model = Query4
		fields = [
			'date1',
			'date2'
		]
class Query5Form(forms.ModelForm):
	class Meta:
		model = Query5
		fields = [
			'date1',
			'x1',
			'x2',
			'y1',
			'y2'
		]

class Query6Form(forms.ModelForm):
	class Meta:
		model = Query6
		fields = [
			'date1',
			'date2'
		]
class Query9Form(forms.ModelForm):
	class Meta:
		model = Query9
		fields = [
			'number'
		]
class Query10Form(forms.ModelForm):
	class Meta:
		model = Query10
		fields = [
			'number'
		]

class Query11Form(forms.ModelForm):
	class Meta:
		model = Query11
		fields = [
			'number'
		]



class AddGeneralForm(forms.ModelForm):
	class Meta:
		model = Add_RequestsGeneralInfo
		fields = [
			'request_id',
			'creation_date',
			'status',
			'completion_date',
			'service_request_number',
			'type_of_service_request'
		]

class AddGeoForm(forms.ModelForm):
	class Meta:
		model = Add_RequestsGeo
		fields = [
			'street_address',
			'zip_code',
			'wards',
			'police_district',
			'community_area',
			'latitude',
			'longitude',
			'zip_codes',
			'historical_wards',
			'community_areas',
			'census_tracts',
			'ward',
			'ssa',
			'y_coordinate',
			'x_coordinate',
			'req_location'
		]
class Add_AbandodedBuildingsForm(forms.ModelForm):
	class Meta:
		model = Add_AbandodedBuildings
		fields = [
			'location_of_building',
			'building_hazardous',
			'building_open',
			'entry_point',
			'vacant_occupied',
			'vacant_due_to_fire',
			'people_using_property'
		]
class Add_AbandonedVehiclesForm(forms.ModelForm):
	class Meta:
		model = Add_AbandonedVehicles
		fields = [
			'license_plate',
			'vehicle_model',
			'vehicle_color',
			'current_activity',
			'most_recent_action',
			'days_reported_parked'
		]
class Add_GarbageCartsForm(forms.ModelForm):
	class Meta:
		model = Add_GarbageCarts
		fields = [
			'number_of_black_carts_delivered',
			'current_activity',
			'recent_action'
		]
class Add_GraffitiRemovalForm(forms.ModelForm):
	class Meta:
		model = Add_GraffitiRemoval
		fields = [
			'type_of_surface',
			'where_is_located'
		]

class Add_PotHolesForm(forms.ModelForm):
	class Meta:
		model = Add_PotHoles
		fields = [
			'current_activity',
			'recent_action',
			'number_of_potholes_filled_on_block'
		]
class Add_RodentBaitingForm(forms.ModelForm):
	class Meta:
		model = Add_RodentBaiting
		fields = [
			'number_of_premises_baited',
			'number_of_premises_with_garbage',
			'number_of_premises_with_rats',
			'current_activity',
			'recent_action'
		]

class Add_SanitationCodeComplaintsForm(forms.ModelForm):
	class Meta:
		model = Add_SanitationCodeComplaints
		fields = [
			'nature_of_code_violation'
		]

class Add_TreeDerbisForm(forms.ModelForm):
	class Meta:
		model = Add_TreeDerbis
		fields = [
			'debris_location',
			'current_activity',
			'most_recent_action'
		]

class Add_TreeTrimsForm(forms.ModelForm):
	class Meta:
		model = Add_TreeTrims
		fields = [
			'trees_location'
		]

