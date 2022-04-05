import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
THINGSBOARD_HOST = 'demo.thingsboard.io' # URL
ACCESS_TOKEN= 'dOmbXs4CQOkESLFf5Rz9'

sensor_data = {'MotorTemp': 0, 'BmsTemp': 0,'Speed':0} # device names
client = mqtt.Client()  # here we getting the instance of client, one time invoking the client object to avoid lack of memory
client.username_pw_set(ACCESS_TOKEN) # username should be a access token in thingsbaord for connection
client.connect(THINGSBOARD_HOST, 1883, 60) # defining port number
client.loop_start() # starting a loop inorder to observe the call backs
motorTemp = 30
bmsTemp = 50
speed = 1

try:
    while True:
        motorTemp = motorTemp * (0.5 + random.random())
        print(motorTemp)
        bmsTemp = bmsTemp * (0.5 + random.random())
        print(bmsTemp)
        if (speed > 150):
            speed = speed * (0.2 + random.random())
        elif (speed > 100 and speed < 150):
            speed = speed * (0.9 + random.random())
        else:
            speed = speed * (2.5 + random.random())
        print(speed)

        sensor_data["MotorTemp"] = motorTemp # sensor_data is variable
        sensor_data["BmsTemp"]   = bmsTemp # sensor_data is variable
        sensor_data["Speed"]     = speed  # sensor_data is variable

        client.publish('v1/devices/me/telemetry',  json.dumps(sensor_data), 1) # topic like ID
        time.sleep(5) # giving a sleep time for the connection to setup

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
