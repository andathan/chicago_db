#!/usr/bin/env python
# coding: utf-8

# In[1]:


#WHEN RUNNING WATCH OUT FOR SSA!!
#change: GEO FIELDS, SSA = -1 , data.columns
#eimai sto "311-service-requests-tree-debris.csv" (den to exw kanei akoma). to neo target index tha einai 3738153
import pandas as pd
from numpy import nan

target = "311-service-requests-vacant-and-abandoned-buildings-reported.csv"
target_index = 4264524 + 1
#info_fields =
info_fields = ['Creation Date','Service Request Number', 'Type of Service Request']
#geo fields with SSA
#geo_fields = ['Street Address','ZIP Code','X Coordinate','Y Coordinate','Wards','Police District','Community Area','Latitude','Longitude','Location','Historical Wards 2003-2015','Zip Codes','Community Areas','Census Tracts','Ward','SSA']
#without SSA:
#geo_fields = ['Street Address','ZIP Code','X Coordinate','Y Coordinate','Wards','Police District','Community Area','Latitude','Longitude','Location','Historical Wards 2003-2015','Zip Codes','Community Areas','Census Tracts','Ward']
geo_fields = ['Street Address','ZIP Code','X Coordinate','Y Coordinate','Ward','Police District','Community Area','Latitude','Longitude','Location']
    
#with SSA:
#geo_fields = ['Street Address','ZIP Code','X Coordinate','Y Coordinate','Wards','Police District','Community Area','Latitude','Longitude','Location','Historical Wards 2003-2015','Zip Codes','Community Areas','Census Tracts','Ward','SSA']

#special fields
#change to: correct special fields
special_fields = ['LOCATION OF BUILDING ON THE LOT (IF GARAGE CHANGE TYPE CODE TO BGD)','IS THE BUILDING DANGEROUS OR HAZARDOUS?','IS BUILDING OPEN OR BOARDED?','IF THE BUILDING IS OPEN WHERE IS THE ENTRY POINT?','IS THE BUILDING CURRENTLY VACANT OR OCCUPIED?','IS THE BUILDING VACANT DUE TO FIRE?','ANY PEOPLE USING PROPERTY? (HOMELESS CHILDEN GANGS)']
#special_fields = "none"





data = pd.read_csv(target,usecols = info_fields,index_col= False)
data.index += target_index
print(data.head(10))
data.index.name = "request_id"
data.to_csv('out_general_info.csv')
del data


data = pd.read_csv(target,usecols = geo_fields,index_col= False)
data.index += target_index
#TO SSA PAEI PRIN APO TO LATITUDE SE OSA EXOUN SSA
data['Community Areas'] = nan
data['Zip Codes']= nan
data['Historical Wards 2003-2015'] = nan
data['Census Tracts'] = nan
data['Wards'] = nan

data.columns = ['Street Address', 'ZIP Code', 'X Coordinate', 'Y Coordinate', 'Ward',
       'Police District', 'Community Area','Latitude', 'Longitude',
       'req_location', 'Historical Wards 2003-2015', 'Zip Codes',
       'Community Areas', 'Census Tracts', 'Wards']
data["SSA"] = -1; 
data = data[['Street Address','ZIP Code','Wards','Police District','Community Area','Latitude','Longitude','Historical Wards 2003-2015','Zip Codes','Community Areas','Census Tracts','Ward','SSA','X Coordinate','Y Coordinate','req_location']]
print(data.head(10))
data.index.name = "request_id"
data.to_csv('out_geo.csv')
del data

if (special_fields != "none"):
    data = pd.read_csv(target,usecols = special_fields,index_col= False)
    data.index += target_index
    #CHANGE TO: correct naming
    data.columns = ['location_of_building','building_hazardous','building_open','entry_point','vacant_occupied','vacant_due_to_fire','people_using_property']
    print(data.head(10))
    data.index.name = "request_id"
    data.to_csv('out_special.csv')


# In[ ]:




