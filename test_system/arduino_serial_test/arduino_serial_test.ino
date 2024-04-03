void setup() {
  // Start the serial communication with the baud rate specified in your Python script
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming data
    String incomingData = Serial.readStringUntil('\n');

    // Send back a response
    if(incomingData == "MEASURE"){
      Serial.println("8 ");
    }
    delay(1000);
  }
}
