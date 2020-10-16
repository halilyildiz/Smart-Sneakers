#include "I2Cdev.h" //I2C kütüphanesi
#include "MPU6050.h" //Mpu6050 kütüphanesi
#include "Wire.h"
#include <SoftwareSerial.h>

MPU6050 accelgyro; // Mpu6050 sensör tanımlama
int16_t ax, ay, az; //ivme tanımlama
int16_t gx, gy, gz; //gyro tanımlama

int16_t axFinal, ayFinal, azFinal; //yazdırılacak ivme tanımlama
int16_t gxFinal, gyFinal, gzFinal; //yazdırılacak gyro tanımlama

//ivme offset değerleri tanımlama
int16_t axOffset = 0; 
int16_t ayOffset = 0;
int16_t azOffset = 0;

//gyro offset tanımlama
int16_t gxOffset = -200;
int16_t gyOffset = -480;
int16_t gzOffset = 50; 

unsigned long previousMillis = 0; //Önceki millis değeri değişkeni
const long interval = 100;        //Ölçümler arasındaki süre (ms)  

#define rxPin 10
#define txPin 11

SoftwareSerial mySerial =  SoftwareSerial(rxPin, txPin);

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
  accelgyro.initialize();
  #define pin modes for tx, rx:
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  //set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
}

void loop() {

  unsigned long currentMillis = millis();  //Millis değeri alınır

  if (currentMillis - previousMillis >= interval) {  //İnterval süresi geçtiğinde içeri girilir
  previousMillis = currentMillis;
    
    // put your main code here, to run repeatedly:
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz); // ivme ve gyro değerlerini okuma
    
    axFinal = ax + axOffset;
    ayFinal = ay + ayOffset;
    azFinal = az + azOffset;
    gxFinal = gx + gxOffset;
    gyFinal = gy + gyOffset;
    gzFinal = gz + gzOffset;

    
    //açısal ivmeleri ve gyro değerlerini ekrana yazdırma 
    mySerial.print(currentMillis); mySerial.print(" ");
    mySerial.print(axFinal); mySerial.print(" ");
    mySerial.print(ayFinal); mySerial.print(" ");
    mySerial.print(azFinal); mySerial.print(" ");
    mySerial.print(gxFinal); mySerial.print(" ");
    mySerial.print(gyFinal); mySerial.print(" ");
    mySerial.print(gzFinal); mySerial.print(" 1");
    mySerial.println();  
  } 

}
