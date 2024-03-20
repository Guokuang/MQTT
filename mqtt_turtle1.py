import paho.mqtt.client as mqtt
import turtle

'''
turtle.goto(12,34) #将画笔移动到坐标 (x：12,y:34) 的位置
turtle.color("green") # 设置画笔颜色为绿色
turtle.goto(56,78)  #将画笔移动到坐标 (56,78) 的位置

turtle.mainloop() #启动图形窗口的主事件循环
'''

mqtt = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_id="dgk_mqtt_turtle")
mqtt.connect("srv-lora")

def on_message_callback(client,userdata,message):
    valeur = message.payload.decode('utf8')
    if valeur == "quit":
        print("fin")
        turtle.done()
        exit(0)
    print(f"topic reçu =>{message.topic}\n msg ==>{valeur}")

    msg = valeur.split(":")
    print("f{msg}")

    if msg[0] == "p":
        turtle.goto(int(msg[1]),int(msg[2]))

    if msg[0] == "c":
        turtle.color(msg[1])

        
mqtt.on_message = on_message_callback
mqtt.subscribe("#")
print("Démarrage de MQTT...")
client.loop_start() # 在另一个线程里面启动

turtle.mainloop()
print("Fin d'éxecution")



