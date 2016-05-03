// set each pixel to one color on the color wheel
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int colorIncrment = 255/NUMBER_PIXELS;  // 1/12th of the way into the color wheel
int hue_sensor_pin = A0;
int sat_sensor_pin = A1;
int bright_sensor_pin = A2;
uint16_t hue_value;
uint8_t sat_value;
uint8_t bright_value;
uint8_t rgb_values[3];

void setup() {
  pinMode(LEDPIN, OUTPUT);
  pinMode(hue_sensor_pin, INPUT);
  pinMode(sat_sensor_pin, INPUT);
  pinMode(bright_sensor_pin, INPUT);
  analogReference(EXTERNAL);
  strip.begin(); // initialize the strip
  // show a white test pattern
  for (int i=0; i<=NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 100, 100, 100);
  }
  strip.show();
  Serial.begin(9600);
  delay(500);
}

void loop() {
  // values should be from 0-1024
   hue_value = analogRead(hue_sensor_pin);
   sat_value = analogRead(sat_sensor_pin);
   bright_value = analogRead(bright_sensor_pin);
   
   hue_value = map(hue_value, 0, 1023, 0, 767);
   sat_value = map(sat_value, 0, 65, 0, 256);
   bright_value = map(bright_value, 0, 63, 0, 256);
   
   Serial.print("hue=");
   Serial.print(hue_value);
   Serial.print(" sat=");
   Serial.print(sat_value);
   Serial.print(" bright=");
   Serial.println(bright_value);
   
   // do conversion
   hsb2rgb(hue_value, sat_value, bright_value, rgb_values);
   
   Serial.print("red=");
   Serial.print(rgb_values[0]);
   Serial.print(" green=");
   Serial.print(rgb_values[1]);
   Serial.print(" blue=");
   Serial.println(rgb_values[2]);
   Serial.println("");
   
   for (int i=0; i<=NUMBER_PIXELS; i++) {
      strip.setPixelColor(i, rgb_values[0], rgb_values[1], rgb_values[2]);
   }
   strip.show();
}

void hsb2rgb(uint16_t index, uint8_t sat, uint8_t bright, uint8_t color[3])
{
	uint16_t r_temp, g_temp, b_temp;
	uint8_t index_mod;
	uint8_t inverse_sat = (sat ^ 255);

	index = index % 768;
	index_mod = index % 256;

	if (index < 256)
	{
		r_temp = index_mod ^ 255;
		g_temp = index_mod;
		b_temp = 0;
	}

	else if (index < 512)
	{
		r_temp = 0;
		g_temp = index_mod ^ 255;
		b_temp = index_mod;
	}

	else if ( index < 768)
	{
		r_temp = index_mod;
		g_temp = 0;
		b_temp = index_mod ^ 255;
	}

	else
	{
		r_temp = 0;
		g_temp = 0;
		b_temp = 0;
	}

	r_temp = ((r_temp * sat) / 255) + inverse_sat;
	g_temp = ((g_temp * sat) / 255) + inverse_sat;
	b_temp = ((b_temp * sat) / 255) + inverse_sat;

	r_temp = (r_temp * bright) / 255;
	g_temp = (g_temp * bright) / 255;
	b_temp = (b_temp * bright) / 255;

	color[0] 	= (uint8_t)r_temp;
	color[1]	= (uint8_t)g_temp;
	color[2]	= (uint8_t)b_temp;
}


void hsb2rgbAN2(uint16_t index, uint8_t sat, uint8_t bright, uint8_t color[3]) {
    uint8_t temp[5], n = (index >> 8) % 3;
// %3 not needed if input is constrained, but may be useful for color cycling and/or if modulo constant is fast
    uint8_t x = ((((index & 255) * sat) >> 8) * bright) >> 8;
// shifts may be added for added speed and precision at the end if fast 32 bit calculation is available
    uint8_t s = ((256 - sat) * bright) >> 8;
    temp[0] = temp[3] =              s;
    temp[1] = temp[4] =          x + s;
    temp[2] =          bright - x    ;
    color[0]  = temp[n + 2];
    color[1] = temp[n + 1];
    color[2]  = temp[n    ];
}
