import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,client_id="GuoKuang2")
client.connect("srv-lora")

def on_message_callback(client_inst,userdata,message):
    v = message.payload.decode('ansi')
    print(f"topic reçu =>{message.topic}\n msg ==>{v}")
    if v == "fin":
        exit()

client.on_message = on_message_callback

client.subscribe("#")
print("Demarrage de MQTT....")
client.loop_forever()
print("Fin d'execution")