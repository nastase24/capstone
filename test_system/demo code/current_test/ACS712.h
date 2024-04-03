// reference: circuito.io and ACS712 library
/** \addtogroup ACS712 
 *  @{
 */
 
#ifndef _ACS712_H_
#define _ACS712_H_

#include "AnalogReader.h"

#define FACTOR 0.026; //26.4mA per count
#define CALREADINGS 1000
#define CALFACTOR 513

class ACS712 : public AnalogReader {
	public:
		ACS712(const int pin);
    void calibrate(int calFactor = CALFACTOR);
    float getCurrent(int cals = CALREADINGS);
  private:
    int m_calFactor = 513;
    float sensitivity = 0.066;
    const float vcc = 5.0;
    const float max = 1023.0;
};

#endif // _ACS712_H_
/** @}*/
