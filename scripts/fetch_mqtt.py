# Python
import json

# Library
import paho.mqtt.client as mqtt

# Application
from app.dashboard.app_models.dashboard import SensorCurrentValue, SensorValue


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("reina/sensorvalue")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode("utf-8"))
    set_current_value(data_sensor=data)    
    save_value_sensor(data_sensor=data)

def set_current_value(data_sensor):
    data = SensorCurrentValue.objects.get(pk=1)
    data.value_tds = data_sensor['tds']
    data.value_ph = data_sensor['ph']
    data.value_humidity = data_sensor['humidity']
    data.value_water_temperature = data_sensor['water_temperature']
    data.value_air_temperature = data_sensor['air_temperature']
    data.save()

def save_value_sensor(data_sensor):
    data = SensorValue()
    data.user_id = 1
    data.value_tds = data_sensor['tds']
    data.value_ph = data_sensor['ph']
    data.value_humidity = data_sensor['humidity']
    data.value_water_temperature = data_sensor['water_temperature']
    data.value_air_temperature = data_sensor['air_temperature']
    data.save()
    
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("sibadaring.com", 1883, 60)
client.loop_forever()