import paho.mqtt.client as mqtt

broker_address = "localhost" # Or your broker's IP/hostname
port = 1883
topic = "my/sensor/data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client("PythonSubscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)
client.loop_forever() # Keep the client running to receive messages