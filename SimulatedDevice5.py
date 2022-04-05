## configuring gateway device
import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

telemetry_data = {
  "a": [
    {
      "ts": 1483228800000,
      "values": {
        "temperature": 42,
        "humidity": 80
      }
    },
  ],
  "b": [
    {
      "ts": 1483228800000,
      "values": {
        "temperature": 42,  
        "humidity": 80
      }
    }
  ]
}

THINGSBOARD_HOST = 'demo.thingsboard.io' # URL
ACCESS_TOKEN= 'iePQullHMCtGlfXCBMxN'
#sensor_data = {'iottemp': 0} # device name
client = mqtt.Client()  # here we getting the instance of client, one time invoking the client object to avoid lack of memory
client.username_pw_set(ACCESS_TOKEN) # username should be a access token in thingsbaord for connection
client.connect(THINGSBOARD_HOST, 1883, 60) # defining port number
client.loop_start() # starting a loop inorder to observe the call backs
try:
    while True:

        senval=random.randrange(0,180)
        print(senval)
        #sensor_data["iottemp"]=senval # sensor_data is variable
        client.publish('v1/gateway/telemetry',  json.dumps(telemetry_data), 1) # topic like ID
        time.sleep(5) # giving a sleep time for the connection to setup
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()

    #pass
