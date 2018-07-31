#Author: Mitchell Palermo
#Last_modified: 3-8-18
#Use: geocode various project locations for display on Tableau map


import geopy
from geopy.geocoders import GoogleV3
import pymssql
import time #library used to make python wait


conn_select = pymssql.connect(server='Server_Name_Here)',user='username',password='Password',database='Database_Name') #connection string
conn_update = pymssql.connect(server='Server_Name_Here',user='username',password='Password',database='Database_Name') #connection string

selectCursor = conn_select.cursor(as_dict=True)#cursor to query database
updateCursor = conn_update.cursor()

#geolocator = GoogleV3(api_key="AIzaSyBrnpHjh5N99TCAet2bZXelv1sK1MTLB-k") #this is the geocoding utility. others can be used as well
geolocator = GoogleV3(api_key="API_Key")


selectCursor.execute('SELECT combinedAddress FROM PR WHERE Latitude IS NULL AND Longitude IS NULL AND combinedAddress IS NOT NULL;')#grabbing data



for row in selectCursor:
	address = row['combinedAddress']
	projectLocation = geolocator.geocode(address)#geocoding happens here
	time.sleep(.500)
	if projectLocation:
		updateCursor.execute("UPDATE PR SET Latitude = {}, Longitude = {} WHERE combinedAddress = '{}';".format(projectLocation.latitude, projectLocation.longitude, address))#inserting the lat and long into table
		#print(projectLocation.latitude, projectLocation.longitude)
		continue

	else:
		print(projectLocation)
		print("This one didn't work")
		continue

conn.commit()
conn.close
