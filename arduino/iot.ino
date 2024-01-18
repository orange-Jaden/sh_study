#include <WiFi.h>
#include <WebSocketsClient.h>  // include before MQTTPubSubClient.h
#include <MQTTPubSubClient.h>

WebSocketsClient client;
MQTTPubSubClient mqtt;

const int LED_PIN = 12;
const char *ssid = "godopu_tele";  // 공유기 와이파이 이름 모든 MQTT공통사항
const char *password = "acgd9488@";    // 공유기 와이파이 비밀번호

void WiFiSetup() {
  Serial.println("start connecting to WiFi");
  // start your network
  WiFi.begin(ssid, password);
  Serial.println("WiFi Connected");
}

void MQTTSetup(){
  Serial.println("start connecting to mqtt broker");

  client.beginSSL("public.cloud.shiftr.io", 443);
  client.setReconnectInterval(2000);

  mqtt.begin(client);
  // connect to mqtt broker
  mqtt.connect("arduino", "public", "public");

  Serial.println("mqtt connected!!");
  // subscribe callback which is called when every packet has come
  mqtt.subscribe([](const String& topic, const String& payload, const size_t size) {
      Serial.println("mqtt received: " + topic + " - " + payload);
  });
  // subscribe topic and callback which is called when /hello has come
  mqtt.subscribe("/shk-iot/led", [](const String& payload, const size_t size) {
      if(payload == "on"){
        Serial.println("ON");
        digitalWrite(LED_PIN, HIGH);
      }else{
        Serial.println("OFF");
        digitalWrite(LED_PIN, LOW);
      }
  });
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  
  // WiFi Setup
  WiFiSetup();
  // MQTT Setup
  MQTTSetup();

  Serial.println("Setup done");
}

void loop() {
    // should be called to trigger callbacks
    mqtt.update();
    delay(1000);
}

