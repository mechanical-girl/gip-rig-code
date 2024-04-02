#include <Servo.h>
#include <HX711.h>

HX711 amp;

// TODO - set actual pins
const int sdaPin = 3;
const int sckPin = 2;

const uint32_t cell_offset = 0;
const uint32_t cell_scale = 0;
const int calibration_weight = 60;  //in grams

void calibrate(HX711 *amp, Stream *Serial) {
  Serial->println("Calibration beginning...");
  Serial->println("Set load to zero. Calibrating in:");
  for (int i = 5; i > 0; i--) {
    Serial->println(i);
  }
  Serial->println("Determining offset now.");
  amp->tare(50);  // take 50 measurements and average them
  uint32_t offset = amp->get_offset();
  Serial->println();
  Serial->println(offset);
  Serial->println();

  Serial->println("Place weight on scale. Getting weight in:");
  for (int i = 5; i > 0; i--) {
    Serial->println(i);
  }
  Serial->print("Determining weight now. Assumes ");
  Serial->print(calibration_weight);
  Serial->print("g.");
}

void setup() {
  // Initialise serial, await readability;
  Serial.begin(115200);
  while (!Serial.available()) {};

  amp.begin(sdaPin, sckPin);

  if (cell_offset == 0 || cell_scale == 0) {
    calibrate(&amp, &Serial);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}
