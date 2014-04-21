#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
float theta1;
float theta2;
float theta3;
String input_string;

void populate_image();

void setup() {
  Serial.begin(9600);
  servo1.attach(2,750,2200);
  servo2.attach(3,750,2200);
  servo3.attach(4,750,2200);
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
  
  pinMode(13, OUTPUT);
  
  theta1 = 0;
  theta2 = 0;
  theta3 = 0;
  
  Serial.write('X');
}

void read_in_coordinates()
{
}
  
void loop() {
  if(Serial.available() > 0)
  {
    char input_character = Serial.read();
    //Serial.print(input_character);
    
    //Serial.write(input_character);
    
    if(input_character == '[')
    {
      while(input_character != ']')
      {
        if(Serial.available() > 0)
        {
          input_character = Serial.read();

          if(input_character != ']')
          {
            input_string.concat(input_character);
          }
          
          //C for continue writing input value
          Serial.write('C');
        }
      }
      
      if(input_string.length() > 0)
      {
          char floatbuf[32];
          input_string.toCharArray(floatbuf, sizeof(floatbuf));
          float input_number = atof(floatbuf);
          
          Serial.println(input_number);
          for(int i = 0; i<input_number; i++)
          {
            digitalWrite(13, HIGH);
            delay(1000);
            digitalWrite(13, LOW);
            delay(1000);
          }
      }
    }
    
    //X means the input value has been completely read
    Serial.write('X');
  }
  
  if(false)
  {
    theta1 += 1;
    theta2 += 1;
    theta3 += 1;
    
    if(theta1 < 0) theta1 = 0;
    if(theta2 < 0) theta2 = 0;
    if(theta3 < 0) theta3 = 0;
    if(theta1 > 200) theta1 = 200;
    if(theta2 > 200) theta2 = 200;
    if(theta3 > 200) theta3 = 200;
   
    drive_joints();
  }

  Serial.write('X');
}

/* drive_joints() simply moves servos 1 and 2 */
void drive_joints() {
  servo1.write(theta1);
  servo2.write(theta2);
  servo3.write(theta3);
    
  //Serial.print(theta1);  Serial.print(",");   Serial.print(theta2);  Serial.print(",");  Serial.println(theta3);
  delay(1000);
}
