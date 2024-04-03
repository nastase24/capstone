// reference: circuito.io and ACS712 library
#include "ACS712.h"
#include "Arduino.h"

ACS712::ACS712(const int pin) : AnalogReader(pin)
{
}
/**
 * Manually calibrate current sensor.
 * calFactor - current calibration factor.
 */
void ACS712::calibrate(int calFactor)
{
  
  long rawVal =0;
  for(int i=0 ; i<1000 ; i++)
    rawVal += read();
  int cal = rawVal / 1000;
  Serial.println(cal);
  if(abs(cal - calFactor) < 1)
  {
    Serial.print(F("Your calibration factor is good!"));
  }
  else
  {
    Serial.print(F("Your calibration factor is: "));
    Serial.println(cal);
    Serial.print(F("Update the calFactor variable in top of Firmware.ino and run again."));
    while(true);
  }
  m_calFactor = cal;
}

/**
 * Get averaged current measurment.
 * cals - number of readings to average.
 * Returns - sensed current in Ampere.
 */
float ACS712::getCurrent(int cals)
{
  float tot_adc = 0;
  for(int i = 0; i < cals; i++){
    tot_adc += read();
  }  
  float adc = tot_adc / float(cals);  
  float voltage = adc * vcc / max;
  float current = (voltage - (vcc / 2)) / sensitivity;
  return current;
}

