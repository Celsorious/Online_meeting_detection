#include <Arduino.h>

const int PIN_red = 3;
const int PIN_green = 10;

void setup() {
  Serial.begin(9600);

  pinMode(PIN_red, OUTPUT);
  pinMode(PIN_green, OUTPUT);

}

void loop() {
  if (Serial.available()>0) {
    char option = Serial.read();
    // Microphone and webcam disconnected
    if (option == '0'){
      digitalWrite(PIN_green, 255);
      digitalWrite(PIN_red, 0);
    }
    // Microphone connected and webcam disconnected
    if(option == '1'){
      digitalWrite(PIN_red, 255);
      digitalWrite(PIN_green, 255);
    }
    // Microphone connected and webcam disconnected
    if(option == '2'){
      digitalWrite(PIN_red, 255);
      digitalWrite(PIN_green, 0);
    }
  }
}

