//Author: Alex Nastase, reference source - www.circuitschools.com
//This program takes a DC voltage measurement once per minute to the serial monitor.

#include <Wire.h>
 
// Define analog input
#define SIGNAL_PIN A1
 
// ADC voltage & Input voltage variables
float adc_voltage = 0.0;
float in_voltage = 0.0;
 
// resistor values in the voltage sensor
float R1 = 30000.0;
float R2 = 7500.0;
 
// the reference voltage of the arduino board
float ref_voltage = 5.0;
 
// integer to collect the adc value
int adc_value = 0;

void setup()
{
  // initialize serial monitor at 9600 baud.
  Serial.begin(9600);
}
 
void loop() {
  // takes the sensor reading from its out pin
  adc_value = analogRead(SIGNAL_PIN);
 
  // convert the analog reading to volts
  adc_voltage  = (adc_value * ref_voltage) / 1024.0;
  in_voltage = adc_voltage / (R2 / (R1 + R2)) ;
 
  // sends the results to serial
  Serial.println(in_voltage, 2);

  // delays for one minute
  delay(60000)
}