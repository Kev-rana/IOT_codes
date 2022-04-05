import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

from Rand_Coor import rand_coor
from Cal_Distance import cal_distance
from No_Of_Cases import no_of_cases
from Patient_Score import patient_score
from Reverse_Geocoder import reverseGeocode

## configuring gateway devic
location = "Dilli 32"
lat = 28.66229
lon = 77.30197
cscore = 55
hr = 0
places = ("Lotus Temple","Akshardham","India Gate","Qutub Minar","Garden of Five Senses","Agrasen ki Baoli","Humayun’s Tomb","Red Fort","Chandni Chowk","Dilli Haat","Lodhi Garden","National Gallery of Modern Art (NGMA)","Tughlaqabad Fort","Tomb of Safdarjang","Purana Qila","India Habitat Centre","Rashtrapati Bhawan","Bangla Sahib Gurudwara","Rajghat","National Zoological Park","Hauz Khas Village","Deer Park","ISKCON Temple",'Worlds of Wonder','Noida Golf Course','Brahmaputra Market','Stupa 18 Gallery','Buddh International',"Botanic Garden of Indian Republic","Okhla Bird Sanctuary","Rashtriya Dalit Prerna Sthal" ,"Green Garden",'Smaaash	DLF Mall of India', 'Snow World	DLF Mall of India','Kidzania','The Great India Place','The Grand Venice Mall','The Great India Place','Atta Market','Appu Ghar Express	The Great India Place','ISKCON','E.d','Desi Vibes','The Yellow Chilli','Filmy Flavours','Barbeque Nation','Noida Pub Exchange','Time Machine','SkyHouse','The Irish House','I Sacked Newton')

## giving initial values to the variables
ulat = lat
ulon = lon
ucscore = cscore
uhr = hr
ulocation =location

alat = lat
alon = lon
acscore = cscore
ahr = hr
alocation =location

dlat = lat
dlon = lon
dcscore = cscore
dhr = hr
dlocation =location


klat = lat
klon = lon
kcscore = cscore
khr = hr
klocation =location

# json format telemetry data of all 4 suspects
telemetry_data = {
  "Urvisha": [
    {
      "ts": 1483228800000,
      "values": {
        "latitude": ulat,
        "longitude": ulon,
        "covid_score": ucscore,
        "time_hrs": uhr,
        "location_details":ulocation
      }
    }
  ],
  "Advait": [
    {
      "ts": 1483228800000,
      "values": {
        "latitude": alat,
        "longitude":alon,
        "covid_score":acscore,
        "time_hrs": ahr,
        "location_details":alocation
      }
    }
  ],
  "Dhruv": [
    {
      "ts": 1483228800000,
      "values": {
        "latitude": dlat,
        "longitude":dlon,
        "covid_score":dcscore,
        "time_hrs": dhr,
        "location_details":dlocation
      }
    }
  ],
  "Kev": [
    {
      "ts": 1483228800000,
      "values": {
        "latitude": klat,
        "longitude": klon,
        "covid_score": kcscore,
        "time_hrs": khr,
        "location_details":klocation
      }
    }
  ],
}

#THINGSBOARD_HOST = 'demo.thingsboard.io' # URL for thingsboard demo(online)
#THINGSBOARD_HOST = 'thingsboard.cloud' # URL for thingsboard cloud, this one is paid 
THINGSBOARD_HOST = 'localhost' # URL for the local host on http://localhost:8080


#ACCESS_TOKEN= 'bvathvZLYtzr6l8OXeeE'
#ACCESS_TOKEN= 'iePQullHMCtGlfXCBMxN'
ACCESS_TOKEN = 'CBSIjS8FPgr2glY1WPfr'

# sensor_data = {'iottemp': 0} # device name
client = mqtt.Client()  # here we getting the instance of client, one time invoking the client object to avoid lack of memory
client.username_pw_set(ACCESS_TOKEN) # username should be a access token in thingsbaord for connection
client.connect(THINGSBOARD_HOST, 1883, 60) # defining port number
client.loop_start() # starting a loop inorder to observe the call backs

try:
    while True:
        # need to create a gateway device(on thingsboard) that receives the data for/from all the suspect devices
        client.publish('v1/gateway/telemetry',  json.dumps(telemetry_data), 1) # topic like ID
        time.sleep(10) # giving a sleep time for the connection to setup






        
        coor = rand_coor()
        ulat = coor[0][0]
        ulon = coor[0][1]
        udist = cal_distance(coor)
        uplace_lat = coor[1][0]
        uplace_lon = coor[1][1]
        ucases = no_of_cases()
        ucscore = patient_score(udist, ucases)

        # ulat = round(ulat - random.random() * 0.008, 5) 
        # ulon = round(ulon - random.random() * 0.008, 5)
        #ucscore = round(ucscore + random.randrange(-8,8), 1)
        if (ucscore > 99):
            ucscore = 99
        elif (ucscore < 10):
            ucscore = 10
        uhr = uhr + 1
        ulocation = reverseGeocode((ulat, ulon))
        # ulocation = places[random.randrange(0, len(places))]
        uplace = reverseGeocode((uplace_lat, uplace_lon))

        coor = rand_coor()
        alat = coor[0][0]
        alon = coor[0][1]
        adist = cal_distance(coor)
        aplace_lat = coor[1][0]
        aplace_lon = coor[1][1]
        acases = no_of_cases()
        acscore = patient_score(adist, acases)
        alocation = reverseGeocode((alat, alon))
        aplace = reverseGeocode((aplace_lat, aplace_lon))

        #alat = round(alat - random.random() * 0.008, 5) 
        #alon = round(alon + random.random() * 0.008, 5)
        #acscore = round(acscore + random.randrange(-8,8), 1)
        if (acscore > 99):
            acscore = 99
        elif (acscore < 10):
            acscore = 10
        ahr = ahr + 1
        #alocation = places[random.randrange(0, len(places))]
        

        coor = rand_coor()
        dlat = coor[0][0]
        dlon = coor[0][1]
        ddist = cal_distance(coor)
        dplace_lat = coor[1][0]
        dplace_lon = coor[1][1]
        dcases = no_of_cases()
        dcscore = patient_score(ddist, dcases)

        #dlat = round(dlat + random.random() * 0.008, 5) 
        #dlon = round(dlon - random.random() * 0.008, 5)
        #dcscore = round(dcscore * random.random(), 1)
        #dcscore = round(dcscore + random.randrange(-8,8), 1)
        if (dcscore > 99):
            dcscore = 99
        elif (dcscore < 10):
            dcscore = 10
        dhr = dhr + 1
        #dlocation = places[random.randrange(0, len(places))]        
        dlocation = reverseGeocode((dlat, dlon))
        dplace = reverseGeocode((dplace_lat, dplace_lon))
        
        coor = rand_coor()
        klat = coor[0][0]
        klon = coor[0][1]
        kdist = cal_distance(coor)
        kplace_lat = coor[1][0]
        kplace_lon = coor[1][1]
        kcases = no_of_cases()
        kcscore = patient_score(kdist, kcases)

        #klat = round(klat + random.random() * 0.008, 5) 
        #klon = round(klon + random.random() * 0.008, 5)
        #kcscore = round(kcscore + random.randrange(-8,8), 1)
        if (kcscore > 99):
            kcscore = 99
        elif (kcscore < 10):
            kcscore = 10
        khr = khr + 1
        # klocation = places[random.randrange(0, len(places))]
        klocation = reverseGeocode((klat, klon))
        kplace = reverseGeocode((kplace_lat, kplace_lon))

        print(ulat, ulon ,ucscore, uhr ,ulocation, uplace)
        print(alat, alon ,acscore, ahr ,alocation, aplace)
        print(dlat, dlon ,dcscore, dhr ,dlocation, dplace)
        print(klat, klon ,kcscore, khr ,klocation, kplace)
        print("----------------------------------------------")
        
        # update the telemetry data 
        telemetry_data = {
        "Urvisha": [
            {
            "ts": 1483228800000,
            "values": {
                "latitude": ulat,
                "longitude": ulon,
                "covid_score": ucscore,
                "time_hrs": uhr,
                "location_details":ulocation
            }
            }
        ],
        "Advait": [
            {
            "ts": 1483228800000,
            "values": {
                "latitude": alat,
                "longitude":alon,
                "covid_score":acscore,
                "time_hrs": ahr,
                "location_details":alocation
            }
            }
        ],
        "Dhruv": [
            {
            "ts": 1483228800000,
            "values": {
                "latitude": dlat,
                "longitude":dlon,
                "covid_score":dcscore,
                "time_hrs": dhr,
                "location_details":dlocation
            }
            }
        ],
        "Kev": [
            {
            "ts": 1483228800000,
            "values": {
                "latitude": klat,
                "longitude": klon,
                "covid_score": kcscore,
                "time_hrs": khr,
                "location_details":klocation
            }
            }
        ],
        }

#        senval=random.randrange(0,180)
#        print(senval)
        #sensor_data["iottemp"]=senval # sensor_data is variable

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    #pass
