#include "Arduino.h"

#define SENSOR_OUTPUT A0

unsigned int sample;

void setup() {
    Serial.begin(9600);
}

void loop() {
    sample = analogRead(SENSOR_OUTPUT);
    Serial.println(sample);
    delay(100);
}