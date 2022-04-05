import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
THINGSBOARD_HOST = 'demo.thingsboard.io' # URL
ACCESS_TOKEN= 'OV3FI42RrQsYHIKiuivy'
sensor_data = {'iottemp': 0} # device name
client = mqtt.Client()  # here we getting the instance of client, one time invoking the client object to avoid lack of memory
client.username_pw_set(ACCESS_TOKEN) # username should be a access token in thingsbaord for connection
client.connect(THINGSBOARD_HOST, 1883, 60) # defining port number
client.loop_start() # starting a loop inorder to observe the call backs
try:
    while True:
        senval=random.randrange(0,180)
        print(senval)
        sensor_data["iottemp"]=senval # sensor_data is variable
        client.publish('v1/devices/me/telemetry',  json.dumps(sensor_data), 1) # topic like ID
        time.sleep(5) # giving a sleep time for the connection to setup
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()

    #pass

