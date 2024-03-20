import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,client_id="GuoKuang")
client.connect("srv-lora")

client.publish(topic="LiMouzheng",payload="p:61:-53")

