import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.payload))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


# 새로운 클라이언트 생성
def NewClient():
    client = mqtt.Client(transport="websockets")
    # client.username_pw_set("etrimqtt", "fainal2311")
    client.username_pw_set("public", "public")
    client.tls_set()
    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    client.on_message = on_message
    # address : localhost, port: 1883 에 연결
    client.connect('public.cloud.shiftr.io', 443)

    return client

client = NewClient()
client.subscribe('/shk-iot/led', 0)
client.loop_forever()