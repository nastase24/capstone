// Author: Alex Nastase
//This program takes a measurement from the AC voltage sensor ZMPT101B
// and sends the values once per minute to the serial monitor.
//and send
#include <ZMPT101B.h>

#define SENSITIVITY 500.0f


void setup() {
  Serial.begin(9600);
  // Change the sensitivity value based on value you got from the calibrate
  // example.
  // ZMPT101B sensor output connected to analog pin A0
  // and the voltage source frequency is 60 Hz in the US.
  ZMPT101B voltageSensor(A1, 60.0);

  voltageSensor.setSensitivity(SENSITIVITY);
}

void loop() {
  // read the voltage and then print to Serial for reciept by RPI
  float voltage = voltageSensor.getRmsVoltage();
  Serial.println(voltage);

  //delay for one minute
  delay(60000);
}
