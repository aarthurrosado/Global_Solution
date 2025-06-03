
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include "DHT.h"

#define DHTPIN 26
#define DHTTYPE DHT22
#define CHUVA_PIN 17  

DHT dht(DHTPIN, DHTTYPE);
Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);

  dht.begin();
  Wire.begin(22, 23);  
  pinMode(CHUVA_PIN, INPUT_PULLUP);

  if (!mpu.begin()) {
    Serial.println("Erro ao iniciar o MPU6050!");
    while (1);
  }
}

void loop() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();

  bool chovendo = digitalRead(CHUVA_PIN) == LOW;
  const char* chuva_txt = chovendo ? "Chovendo" : "Sem chuva";

  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Serial.printf(
    "Temp: %.1f°C | Umidade: %.1f%% | Chuva: %s | Acc X: %.2f | Y: %.2f | Z: %.2f\n",
    temperatura,
    umidade,
    chuva_txt,
    a.acceleration.x,
    a.acceleration.y,
    a.acceleration.z
  );

  delay(2000);
}
