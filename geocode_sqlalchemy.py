#Author: Mitchell Palermo
#Last_modified: 3-8-18
#Use: geocode various project locations for display on Tableau map

import time #library used to make python wait
import geopy
from geopy.geocoders import GoogleV3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base  = declarative_base()

engine = create_engine('mssql+pymssql:<connectionString>', echo=True)

class Project(Base): #defining a class that will map to a table
 __tablename__ = "PR"

 projectNumber = Column('WBS1', String, ForeignKey=True)
 name = Column('Name',String)
 combinedAddress = Column('combinedAddress', String)


class CustValues(Base): #defining class for custom value table
 __tablename__="ProjectCustomTabFields"
 projectNumber = Column('WBS1', String, primary_key=True)
 latitude = Column('CustLatitude', String)
 longitude = Column('CustLongitude',String)





Session = sessionmaker(bind=engine)
geolocator = GoogleV3(api_key="API_Key")

session = Session()

for instance in session.query(Project).filter(Project.combinedAddress != None).filter(Project.Latitude == None).filter(Project.projectNumber.like('%P')):
#this loop
   processedAddress = geolocator.geocode(instance.combinedAddress,timeout=None)#geocode combinedAddress
   time.sleep(.300)#pause for 300 miliseconds
   if processedAddress:#if geocoding works
         session.query(CustValues).filter(CustValues.WBS1 == instance.WBS1)\
         .update({'CustLongitude' : processedAddress.longitude,'CustLatitude' : processedAddress.latitude})
         #Project.update().values(Longitude=processedAddress.longitude).where(combinedAddress!= None)

         session.commit()#commit all changes

session.close()
