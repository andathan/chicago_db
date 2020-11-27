"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chicago import views
from chicago.views import *
urlpatterns = [
    
    path('search_street_form.html', views.search_street_form, name= 'search_street_form'),
    path('search_street.html', views.search_street, name= 'search_street'),

    path('search_zip_code_form.html', views.search_zip_code_form, name= 'search_zip_code_form'),
    path('search_zip_code.html', views.search_zip_code, name= 'search_zip_code'),

    path('add_geo_form.html', views.add_geo_form_view, name='add_geo_form'),
    path('add_geo.html', views.add_geo_view, name='add_geo'),
    path('add_form.html', views.add_form_view, name='add_form'),
    path('add.html', views.add_view, name='add'),

    path('done.html', views.done_view, name='done'),
    path('add_vacant_building_form.html', views.add_vacant_building_form, name= 'add_vacant_building_form'),
    path('add_vacant_building.html', views.add_vacant_building, name= 'add_vacant_building'),

    path('add_abandoned_vehicle_form.html', views.add_abandoned_vehicle_form, name= 'add_abandoned_vehicle_form'),
    path('add_abandoned_vehicle.html', views.add_abandoned_vehicle, name= 'add_abandoned_vehicle'),

    path('add_garbage_carts_form.html', views.add_garbage_carts_form, name= 'add_garbage_carts_form'),
    path('add_garbage_carts.html', views.add_garbage_carts, name= 'add_garbage_carts'),

    path('add_graffiti_removal_form.html', views.add_graffiti_removal_form, name= 'add_graffiti_removal_form'),
    path('add_graffiti_removal.html', views.add_graffiti_removal, name= 'add_graffiti_removal'),

    path('add_potholes_form.html', views.add_potholes_form, name= 'add_potholes_form'),
    path('add_potholes.html', views.add_potholes, name= 'add_potholes'),

    path('add_rodent_bait_form.html', views.add_rodent_bait_form, name= 'add_rodent_bait_form'),
    path('add_rodent_bait.html', views.add_rodent_bait, name= 'add_rodent_bait'),

    path('add_sanitation_code_form.html', views.add_sanitation_code_form, name= 'add_sanitation_code_form'),
    path('add_sanitation_code.html', views.add_sanitation_code, name= 'add_sanitation_code'),

    path('add_tree_trim_form.html', views.add_tree_trim_form, name= 'add_tree_trim_form'),
    path('add_tree_trim.html', views.add_tree_trim, name= 'add_tree_trim'),

    path('add_tree_debris_form.html', views.add_tree_debris_form, name= 'add_tree_debris_form'),
    path('add_tree_debris.html', views.add_tree_debris, name= 'add_tree_debris'),

    path('', views.home_view, name='home'),
    path('home', views.home_view, name='home'),


    path('query1.html', views.query1_view, name='query1'),
    path('query1_form.html', views.query1_form_view, name='query1_form'),
    path('query2.html', views.query2_view, name='query2'),
    path('query2_form.html', views.query2_form_view, name='query2_form'),
    path('query3.html', views.query3_view, name='query3'),
    path('query3_form.html', views.query3_form_view, name='query3_form'), 
    path('query4.html', views.query4_view, name='query4'),
    path('query4_form.html', views.query4_form_view, name='query4_form'), 
    path('query5.html', views.query5_view, name='query5'),
    path('query5_form.html', views.query5_form_view, name='query5_form'),
    path('query6.html', views.query6_view, name='query6'),
    path('query6_form.html', views.query6_form_view, name='query6_form'),
    path('query7.html', views.query7_view, name='query7'),
    path('query8.html', views.query8_view, name='query8'),
    path('query9.html', views.query9_view, name='query9'),
    path('query9_form.html', views.query9_form_view, name='query9_form'), 
    path('query10.html', views.query10_view, name='query10'),
    path('query10_form.html', views.query10_form_view, name='query10_form'),
    path('query11.html', views.query11_view, name='query11'),
    path('query11_form.html', views.query11_form_view, name='query11_form'),
    path('query12.html', views.query12_view, name='query12'),
    path('admin/', admin.site.urls),



]
