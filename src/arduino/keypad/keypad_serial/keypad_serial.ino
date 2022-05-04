
/*********************************** CIRCUIT **********************************\
| 16 Buttons Mode:                                                             |
|	* TTP229 VCC to pin VCC                                                    |
|	* TTP229 GND to pin GND                                                    |
|	* TTP229 SCL to pin 2                                                      |
|	* TTP229 SDO to pin 3                                                      |
|	* TTP229 TP2 to GND via 1 Megohm resistor!                                 |
|	# See TTP229_Modes.jpg for help...                                         |
|                                                                              |
| Important:                                                                   |
|	* Must reconnect the TTP229 power so the mode changes will take effect     |
|	* The 1 Megohm resistors already exist on some TTP229 modules              |
\******************************************************************************/

#include <TTP229.h>

const int SCL_PIN = A5;  // The pin number of the clock pin.
const int SDO_PIN = A4;  // The pin number of the data pin.

TTP229 ttp229(SCL_PIN, SDO_PIN); // TTP229(sclPin, sdoPin)

void setup()
{
	Serial.begin(115200);
	Serial.println("Start Touching One Key At a Time!");
}

void loop()
{
	//uint8_t key = ttp229.ReadKey16(); // Blocking
   uint8_t key = ttp229.GetKey16(); // Non Blocking

	if (key) Serial.println(key);

  // Serial.println(key);
}


