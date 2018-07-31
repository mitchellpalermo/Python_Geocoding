# GeoCoding with Python

This project contains two different methods of geocoding with Python. One is relatively straightforward, albeit a little more verbose. However, the simpler implementation had a much harder time parsing unorthodox addresses. SQL Alchemy was used to abstract some of the heavy lifting in dealing with database operations. This implementation worked perfectly.  

## Dependencies
-     SQL Alchemy
-     Geopy


There are a variety of Geocoders available to choose from. I used Google Maps because it performed the best and didn’t require payment in order to use. An API key will be necessary in order to use any of them. 