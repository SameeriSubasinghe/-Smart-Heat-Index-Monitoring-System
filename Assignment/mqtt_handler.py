import json
import os

import paho.mqtt.client as paho
from dotenv import load_dotenv
from paho import mqtt

load_dotenv()


def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)


def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


mqtt_broker = os.getenv('MQTT_BROKER')
mqtt_port = int(os.getenv('MQTT_PORT'))
mqtt_topic = os.getenv('MQTT_TOPIC')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

client.username_pw_set(username, password)

client.connect(mqtt_broker, mqtt_port)

client.on_publish = on_publish


def publish_msg(temperature, humidity, heat_index):
    msg = json.dumps({"temperature": temperature,
                      "humidity": humidity,
                      "heat_index": heat_index})

    client.publish(mqtt_topic, payload=msg, qos=1)
