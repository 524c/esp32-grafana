#include <ArduinoJson.h>
#include <HTTPClient.h>
#include <WiFiMulti.h>
 
const char *AP_SSID = "my_ssid";
const char *AP_PWD = "ap_password";
  
WiFiMulti wifiMulti;
 
void setup() {
  Serial.begin(9600);
   
  delay(4000);
  wifiMulti.addAP(AP_SSID, AP_PWD);
 
  postDataToServer();
}
 
void loop() {
  // Not used in this example
}
 
void postDataToServer() {
 
  Serial.println("Posting JSON data to server...");
  // Block until we are able to connect to the WiFi access point
  if (wifiMulti.run() == WL_CONNECTED) {
     
    HTTPClient http;   
     
    http.begin("https://httpbin.org/anything");  
    http.addHeader("Content-Type", "application/json");         

    StaticJsonDocument<200> doc;
    // Add values in the document
    //
    doc["name"] = "esp32";
    doc["sensor1"] = 1; // coletar valor do sensor 1
		doc["sensor2"] = 2; // coletar valor do sensor 2
   
    String requestBody;
    serializeJson(doc, requestBody);
     
    int httpResponseCode = http.POST(requestBody);
 
    if(httpResponseCode>0){
       
      String response = http.getString();                       
       
      Serial.println(httpResponseCode);   
      Serial.println(response);
     
    }
    else {
     
      Serial.printf("Error occurred while sending HTTP POST: %s\n", httpClient.errorToString(statusCode).c_str());
       
    }
     
  }
}