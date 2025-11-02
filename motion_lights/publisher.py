import paho.mqtt.client as mqtt

broker_address = "localhost" # Or your broker's IP/hostname
port = 1883
topic = "my/sensor/data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

client = mqtt.Client("PythonPublisher")
client.on_connect = on_connect
client.connect(broker_address, port)
client.loop_start()

client.publish(topic, "Hello from Python!")
print(f"Published 'Hello from Python!' to topic '{topic}'")

client.loop_stop()
client.disconnect()
