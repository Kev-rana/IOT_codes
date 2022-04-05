import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
THINGSBOARD_HOST = 'demo.thingsboard.io' # URL
ACCESS_TOKENa= 'ejNrkSgrb0RbEUsGGXfp'
ACCESS_TOKENb= '72FRmS9ngky9DQ9WbQTm'

sensor_dataa = {'a' : 0}
sensor_datab = {'b': 0} # device names
clienta = mqtt.Client()  # here we getting the instance of client, one time invoking the client object to avoid lack of memory
clientb = mqtt.Client()  # here we getting the instance of client, one time invoking the client object to avoid lack of memory

clienta.username_pw_set(ACCESS_TOKENa) # username should be a access token in thingsbaord for connection
clientb.username_pw_set(ACCESS_TOKENb) # username should be a access token in thingsbaord for connection


clienta.connect(THINGSBOARD_HOST, 1883, 60) # defining port number
clientb.connect(THINGSBOARD_HOST, 1883, 60) # defining port number

clienta.loop_start() # starting a loop inorder to observe the call backs
clientb.loop_start() # starting a loop inorder to observe the call backs

try:
    while True:
        senval=random.randrange(0,180)
        print('a', senval)
        sensor_dataa["a"]=senval # sensor_data is variable
        clienta.publish('v1/devices/me/telemetry',  json.dumps(sensor_dataa), 1) # topic like ID
        time.sleep(5) # giving a sleep time for the connection to setup
        senval=random.randrange(0,180)
        print('b', senval)
        sensor_datab["b"]=senval # sensor_data is variable
        clientb.publish('v1/devices/me/telemetry',  json.dumps(sensor_datab), 1) # topic like ID
        time.sleep(5) # giving a sleep time for the connection to setup
        print("----------")

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()

    #pass

