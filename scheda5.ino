/*
 * ESP8266 (Adafruit HUZZAH) Mosquitto MQTT Publish Example
 * Thomas Varnish (https://github.com/tvarnish), (https://www.instructables.com/member/Tango172)
 * Made as part of my MQTT Instructable - "How to use MQTT with the Raspberry Pi and ESP8266"
 */
#include <Bounce2.h> // Used for "debouncing" the pushbutton
#include <ESP8266WiFi.h> // Enables the ESP8266 to connect to the local network (via WiFi)
#include <PubSubClient.h> // Allows us to connect to, and publish to the MQTT broker

const int ledPin = 0; // This code uses the built-in led for visual feedback that the button has been pressed
const int buttonPin = 15; // Connect your button to pin #13
const int buttonPin2 = 13;
const int buttonPin3 = 12;
const int buttonPin4 = 14;
int stato = 0;
int a = 0;

// WiFi
// Make sure to update this for your own WiFi network!
const char* ssid = "nome wifi";
const char* wifi_password = "password wifi";

// MQTT
// Make sure to update this for your own MQTT Broker!
const char* mqtt_server = "ip broker";
const char* mqtt_topic = "topic pubblisc";
const char* mqtt_topic_sub = "topic subcrive";
const char* mqtt_username = "nome broker";
const char* mqtt_password = "password broker";
// The client id identifies the ESP8266 device. Think of it a bit like a hostname (Or just a name, like Greg).
const char* clientID = "ESP01";

// Initialise the Pushbutton Bouncer object
Bounce bouncer = Bounce();
Bounce bouncer2 = Bounce();
Bounce bouncer3 = Bounce();
Bounce bouncer4 = Bounce();

// Initialise the WiFi and MQTT Client objects
WiFiClient wifiClient;
PubSubClient client(mqtt_server, 1883, wifiClient); // 1883 is the listener port for the Broker

void ReceivedMessage(char* topic, byte* payload, unsigned int length) {
  // Output the first character of the message to serial (debug)
  Serial.println((char)payload[0]);

  // Handle the message we received
  // Here, we are only looking at the first character of the received message (payload[0])
  // If it is 0, turn the led off.
  // If it is 1, turn the led on.
  if ((char)payload[0] == 'a') { // ritardo scheda 1 primo video 1
    Serial.println("payload a");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 91){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'b') { // ritardo scheda 1 primo video 2
    Serial.println("payload b");
    digitalWrite(ledPin, HIGH);
    delay(1000);
    a = 0;
    while ( a <= 68){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'c') { // ritardo scheda 1 primo video 3
    Serial.println("payload c");
    digitalWrite(ledPin, HIGH);
    delay(1000);
    a = 0;
    while ( a <= 135){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;   
  }
  if ((char)payload[0] == 'd') { // ritardo scheda 1 primo video 4
    Serial.println("payload d");
    digitalWrite(ledPin, HIGH);
    delay(1000);
    a = 0;
    while ( a <= 126){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;   
  }
  if ((char)payload[0] == 'e') {
    Serial.println("payload e");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 187){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'f') {
    Serial.println("payload f");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 183){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'g') {
    Serial.println("payload g");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 144){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'h') {
    Serial.println("payload h");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 170){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'i') {
    Serial.println("payload i");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 138){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'l') {
    Serial.println("payload l");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 59){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'm') {
    Serial.println("payload m");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 244){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'n') {
    Serial.println("payload n");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 109){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'o') {
    Serial.println("payload o");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 13){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'p') {
    Serial.println("payload p");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 13){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'r') {
    Serial.println("payload r");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 13){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 's') {
    Serial.println("payload s");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 13){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 't') {
    Serial.println("payload t");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 13){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'u') {
    Serial.println("payload u");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 13){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'v') {
    Serial.println("payload v");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 13){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'z') {
    Serial.println("payload z");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 15){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
  if ((char)payload[0] == 'x') { // ritardo se pulsante interruzione viene premuto
    Serial.println("payload x");
    digitalWrite(ledPin, HIGH);
    a = 0;
    while ( a <= 2){
      delay (1000);
      a = a + 1;
      }
    digitalWrite(ledPin, LOW);
    stato = 0;
  }
}

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);

  // Switch the on-board LED off to start with
  digitalWrite(ledPin, HIGH);

  // Setup pushbutton Bouncer object
  bouncer.attach(buttonPin);
  bouncer2.attach(buttonPin2);
  bouncer3.attach(buttonPin3);
  bouncer4.attach(buttonPin4);
  bouncer.interval(25);
  bouncer2.interval(25);
  bouncer3.interval(25);
  bouncer4.interval(25);

  // Begin Serial on 115200
  // Remember to choose the correct Baudrate on the Serial monitor!
  // This is just for debugging purposes
  Serial.begin(115200);

  Serial.print("Connecting to ");
  Serial.println(ssid);

  // Connect to the WiFi
  WiFi.begin(ssid, wifi_password);

  // Wait until the connection has been confirmed before continuing
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Debugging - Output the IP Address of the ESP8266
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
client.setCallback(ReceivedMessage);
  // Connect to MQTT Broker
  // client.connect returns a boolean value to let us know if the connection was successful.
  // If the connection is failing, make sure you are using the correct MQTT Username and Password (Setup Earlier in the Instructable)
  if (client.connect(clientID, mqtt_username, mqtt_password)) {
    client.subscribe(mqtt_topic_sub);
    Serial.println("Connected to MQTT Broker!");
  }
  else {
    Serial.println("Connection to MQTT Broker failed...");
  }

}

bool Connect() {
  // Connect to MQTT Server and subscribe to the topic
  Serial.println("boll connet");
  if (client.connect(clientID, mqtt_username, mqtt_password)) {
      client.subscribe(mqtt_topic_sub);
      Serial.println("sottoscritto bool");
      return true;
    }
    else {
      return false;
      Serial.println("bool false");
  }
}


void loop() {
  // Update button state
  // This needs to be called so that the Bouncer object can check if the button has been pressed
  bouncer.update();
  bouncer2.update();
  bouncer3.update();
  bouncer4.update();
  if (stato == 0){
    if (bouncer.rose()) {
      // Turn light on when button is pressed down
      // (i.e. if the state of the button rose from 0 to 1 (not pressed to pressed))
      digitalWrite(ledPin, LOW);
      if (!client.connected()) {
        Connect();
      }
      // PUBLISH to the MQTT Broker (topic = mqtt_topic, defined at the beginning)
      // Here, "Button pressed!" is the Payload, but this could be changed to a sensor reading, for example.
      if (client.publish(mqtt_topic, "Button pressed!")) {
        Serial.println("Button pushed and message sent!");
        stato = 1;
        Serial.println(stato);
      }
      // Again, client.publish will return a boolean value depending on whether it succeded or not.
      // If the message failed to send, we will try again, as the connection may have broken.
      else {
        Serial.println("Message failed to send. Reconnecting to MQTT Broker and trying again");
        client.connect(clientID, mqtt_username, mqtt_password);
        delay(10); // This delay ensures that client.publish doesn't clash with the client.connect call
        client.publish(mqtt_topic, "Button pressed!");
        }
    }
    else if (bouncer.fell()) {
      // Turn light off when button is released
      // i.e. if state goes from high (1) to low (0) (pressed to not pressed)
      digitalWrite(ledPin, HIGH);
    }

    if (bouncer2.rose()) {
      // Turn light on when button is pressed down
      // (i.e. if the state of the button rose from 0 to 1 (not pressed to pressed))
      digitalWrite(ledPin, LOW);
      if (!client.connected()) {
        Connect();
      }
      // PUBLISH to the MQTT Broker (topic = mqtt_topic, defined at the beginning)
      // Here, "Button pressed!" is the Payload, but this could be changed to a sensor reading, for example.
      if (client.publish(mqtt_topic, "Button2 pressed!")) {
        Serial.println("Button pushed2 and message sent!");
        stato = 1;
      }
      // Again, client.publish will return a boolean value depending on whether it succeded or not.
      // If the message failed to send, we will try again, as the connection may have broken.
      else {
        Serial.println("Message failed to send. Reconnecting to MQTT Broker and trying again");
        client.connect(clientID, mqtt_username, mqtt_password);
        delay(10); // This delay ensures that client.publish doesn't clash with the client.connect call
        client.publish(mqtt_topic, "Button2 pressed!");
        }
    }
    else if (bouncer2.fell()) {
      // Turn light off when button is released
      // i.e. if state goes from high (1) to low (0) (pressed to not pressed)
      digitalWrite(ledPin, HIGH);
    }


    if (bouncer3.rose()) {
      // Turn light on when button is pressed down
      // (i.e. if the state of the button rose from 0 to 1 (not pressed to pressed))
      digitalWrite(ledPin, LOW);
      if (!client.connected()) {
        Connect();
      }
      // PUBLISH to the MQTT Broker (topic = mqtt_topic, defined at the beginning)
      // Here, "Button pressed!" is the Payload, but this could be changed to a sensor reading, for example.
      if (client.publish(mqtt_topic, "Button3 pressed!")) {
        Serial.println("Button pushed3 and message sent!");
        stato = 1;
      }
      // Again, client.publish will return a boolean value depending on whether it succeded or not.
      // If the message failed to send, we will try again, as the connection may have broken.
      else {
        Serial.println("Message failed to send. Reconnecting to MQTT Broker and trying again");
        client.connect(clientID, mqtt_username, mqtt_password);
        delay(10); // This delay ensures that client.publish doesn't clash with the client.connect call
        client.publish(mqtt_topic, "Button3 pressed!");
        }
    }
    else if (bouncer3.fell()) {
      // Turn light off when button is released
      // i.e. if state goes from high (1) to low (0) (pressed to not pressed)
      digitalWrite(ledPin, HIGH);
    }


    if (bouncer4.rose()) {
      // Turn light on when button is pressed down
      // (i.e. if the state of the button rose from 0 to 1 (not pressed to pressed))
      digitalWrite(ledPin, LOW);
      if (!client.connected()) {
        Connect();
      }
      // PUBLISH to the MQTT Broker (topic = mqtt_topic, defined at the beginning)
      // Here, "Button pressed!" is the Payload, but this could be changed to a sensor reading, for example.
      if (client.publish(mqtt_topic, "Button4 pressed!")) {
        Serial.println("Button pushed4 and message sent!");
        stato = 1;
      }
      // Again, client.publish will return a boolean value depending on whether it succeded or not.
      // If the message failed to send, we will try again, as the connection may have broken.
      else {
        Serial.println("Message failed to send. Reconnecting to MQTT Broker and trying again");
        client.connect(clientID, mqtt_username, mqtt_password);
        delay(10); // This delay ensures that client.publish doesn't clash with the client.connect call
        client.publish(mqtt_topic, "Button4 pressed!");
        }
    }
    else if (bouncer4.fell()) {
      // Turn light off when button is released
      // i.e. if state goes from high (1) to low (0) (pressed to not pressed)
      digitalWrite(ledPin, HIGH);
    }

    }
  client.loop();
  delay(20);
}
