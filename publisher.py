import paho.mqtt.client as mqtt
from random import randrange,uniform
import time


mqttBroker = 'broker.hivemq.com'
client = mqtt.Client("A simple text")
client.connect(mqttBroker)

text = "This is a demo text that will be published to a public broker"
client.publish("a simple text", text)
print(f"Published '{text}' ")
time.sleep(1)