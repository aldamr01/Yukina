import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("reina/input")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.payload.decode("utf-8"))
    # data = json.loads(msg.payload.decode("utf-8"))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("sibadaring.com", 1883, 60)
client.publish("reina/input", '{"mixin": "on"}', qos=0, retain=False)