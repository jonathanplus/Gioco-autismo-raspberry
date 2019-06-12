#include <Adafruit_NeoPixel.h>
#define PIN 9
// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(37, PIN, NEO_GRB + NEO_KHZ800);
int lettura3Pin = 3;
int lettura4Pin = 4;
int lettura5Pin = 5;
int lettura6Pin = 6;
int temp = 100;
int val = 0;
int stato = 0;
int bin4 = 0;
int bin5 = 0;
int bin6 = 0;

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  strip.setBrightness(50);
  pinMode(lettura3Pin, INPUT_PULLUP);
  pinMode(lettura4Pin, INPUT_PULLUP);
  pinMode(lettura5Pin, INPUT_PULLUP);
  pinMode(lettura6Pin, INPUT_PULLUP);
}
void loop() {

val = digitalRead(lettura3Pin);
if (val == 1){
  stato = 1;
}
if (stato == 1){  
  bin4 = digitalRead(lettura4Pin);
  bin5 = digitalRead(lettura5Pin);
  bin6 = digitalRead(lettura6Pin);
  if (bin4 == 1 and bin5 == 0 and bin6 == 0) {
    colorWipe(strip.Color(  0, 100,   0), 50); // Green
    theaterChase(strip.Color(  0,   100, 0), 50);// verde, half brightness
    colorWipe(strip.Color(  0, 100,   0), 50);
    colorWipo(strip.Color(0,   0,   0), 50);
    stato = 0;
}
  if (bin4 == 1 and bin5 == 1 and bin6 == 0){
    colorWipe(strip.Color(  0,   0, 100), 50); // Blue
    theaterChase(strip.Color(  0,   0, 100), 50);// Blue, half brightness
    colorWipe(strip.Color(  0,   0, 100), 50);
    colorWipo(strip.Color(0,   0,   0), 50);
    stato = 0;
  }
  if (bin4 == 1 and bin5 == 1 and bin6 == 1){
    colorWipe(strip.Color(100,   100,   0), 50); // giallo
    theaterChase(strip.Color(  100,   100, 0), 50);// giallo half brightness
    colorWipe(strip.Color(100,   100,   0), 50);
    colorWipo(strip.Color(0,   0,   0), 50);
    stato = 0;   
}

  if (bin4 == 0 and bin5 == 0 and bin6 == 0){
    colorWipe(strip.Color(100,   0,   0), 50); // Red
    theaterChase(strip.Color(100,   0,   0), 50); // Red, half brightness
    colorWipe(strip.Color(100,   0,   0), 50);
    colorWipo(strip.Color(0,   0,   0), 50);
    stato = 0;
}

  if (bin4 == 0 and bin5 == 1 and bin6 == 1){
    colorWipe(strip.Color(100, 100, 100), 50); // bianco
    theaterChase(strip.Color(100, 100, 100), 50); // bianco brightness
    colorWipe(strip.Color(100, 100, 100), 50);
    colorWipo(strip.Color(0,   0,   0), 50);
    stato = 0;
}

  if (bin4 == 0 and bin5 == 0 and bin6 == 1){
    colorWipe(strip.Color(100,   0,   100), 50); // viola
    theaterChase(strip.Color(100,   0, 100), 50); // viola, half brightness
    colorWipe(strip.Color(100,   0, 100), 50);
    colorWipo(strip.Color(0,   0,   0), 50);
    stato = 0;
}

  if (bin4 == 0 and bin5 == 1 and bin6 == 0){
    theaterChaseRainbow(50); //lampeggio arcobaleno
    rainbow(10); //arcobaleno
    colorWipo(strip.Color(0,   0,   0), 50);
    stato = 0;
}

}
delay (25);
}
void colorWipe(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
    strip.setPixelColor(i, color);         //  Set pixel's color (in RAM)
    strip.show();                          //  Update strip to match
    delay(wait);                           //  Pause for a moment
  }
}
void colorWipo(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
    strip.setPixelColor(i, color);         //  Set pixel's color (in RAM)
    strip.show();                          //  Update strip to match
    delay(wait);                           //  Pause for a moment
  }
}
void theaterChase(uint32_t color, int wait) {
  for(int a=0; a<67; a++) {  // Repeat 10 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      // 'c' counts up from 'b' to end of strip in steps of 3...
      for(int c=b; c<strip.numPixels(); c += 3) {
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show(); // Update strip with new contents
      delay(wait);  // Pause for a moment
    }
  }
}

void rainbow(int wait) {
  // Hue of first pixel runs 5 complete loops through the color wheel.
  // Color wheel has a range of 65536 but it's OK if we roll over, so
  // just count from 0 to 5*65536. Adding 256 to firstPixelHue each time
  // means we'll make 5*65536/256 = 1280 passes through this outer loop:
  for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 256) {
    for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
      // Offset pixel hue by an amount to make one full revolution of the
      // color wheel (range of 65536) along the length of the strip
      // (strip.numPixels() steps):
      int pixelHue = firstPixelHue + (i * 65536L / strip.numPixels());
      // strip.ColorHSV() can take 1 or 3 arguments: a hue (0 to 65535) or
      // optionally add saturation and value (brightness) (each 0 to 255).
      // Here we're using just the single-argument hue variant. The result
      // is passed through strip.gamma32() to provide 'truer' colors
      // before assigning to each pixel:
      strip.setPixelColor(i, strip.gamma32(strip.ColorHSV(pixelHue)));
    }
    strip.show(); // Update strip with new contents
    delay(wait);  // Pause for a moment
  }
}

void theaterChaseRainbow(int wait) {
  int firstPixelHue = 0;     // First pixel starts at red (hue 0)
  for(int a=0; a<30; a++) {  // Repeat 30 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      // 'c' counts up from 'b' to end of strip in increments of 3...
      for(int c=b; c<strip.numPixels(); c += 3) {
        // hue of pixel 'c' is offset by an amount to make one full
        // revolution of the color wheel (range 65536) along the length
        // of the strip (strip.numPixels() steps):
        int      hue   = firstPixelHue + c * 65536L / strip.numPixels();
        uint32_t color = strip.gamma32(strip.ColorHSV(hue)); // hue -> RGB
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show();                // Update strip with new contents
      delay(wait);                 // Pause for a moment
      firstPixelHue += 65536 / 90; // One cycle of color wheel over 90 frames
    }
  }
}
