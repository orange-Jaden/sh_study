import paho.mqtt.client as mqtt
import pygame
from pygame.locals import *

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

mqttClient = NewClient()
mqttClient.loop_start()

pygame.init()

clock = pygame.time.Clock()
fps = 120

screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jaden IoT")

# mqtt client, callback 생성 
def turnOn():
    print("turn on")
    # LED를 켜기 위해 메시지 전송
    client.publish('/shk-iot/led', 'on', 1)

def turnOff():
    print("turn off")
    # LED를 끄기 위해 메시지 전송

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

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

# 새로운 클라이언트 생성
client = mqtt.Client(transport="websockets")
client.username_pw_set("public", "public")
client.tls_set()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_message = on_message
client.connect('public.cloud.shiftr.io', 443)
client.loop_start()

# load images
class Button: 
    def __init__(self, x, y, image, callback):
        pygame.sprite.Sprite.__init__(self)
        self.clicked = False
        self.image = image
        self.callback = callback
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self) -> bool:
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not(self.clicked):
                self.clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                self.callback()
        elif not(self.rect.collidepoint(pos)) and self.clicked:
            self.clicked = False
        
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

# create restart button instance
on_button_img = pygame.image.load('img/btn_on.png')
off_button_img = pygame.image.load('img/btn_off.png')
button1 = Button(screen_width // 2 - 50, screen_height // 2 - 100, on_button_img, turnOn)
button2 = Button(screen_width // 2 - 50, screen_height // 2 + 100, off_button_img, turnOff)

run  = True
while run:
    clock.tick(fps)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    button1.draw()
    button2.draw()

    pygame.display.update()

mqttClient.loop_stop()
mqttClient.disconnect()
pygame.quit()
