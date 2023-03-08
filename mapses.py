# GOOGLE MAPS USING 

import gmaps 

with open('apikey.txt') as f:
    api_key = f.readline()
    f.close

gmaps.configure(api_key='')

new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)