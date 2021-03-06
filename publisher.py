import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

def connect_mqtt():
    """
    It creates a new MQTT client, sets the username and password, and connects to the MQTT broker
    :return: The client object is being returned.
    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    """
    > The function `publish` takes a client as an argument and publishes a message to the topic `topic`
    
    The function `publish` takes a client as an argument and publishes a message to the topic `topic`
    
    :param client: the MQTT client object
    """
    simpleMessage = "This is the simple message to be sent via MQTT"
   
    time.sleep(1)
    msg = f"messages: '{simpleMessage}'"
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
   


def run():
    """
    `run()` connects to the MQTT broker, starts the loop, and publishes a message
    """
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()