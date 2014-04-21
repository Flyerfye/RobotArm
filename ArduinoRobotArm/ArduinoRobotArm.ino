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
  
  theta1 = -1;
  theta2 = -1;
  theta3 = -1;
  
  Serial.write('X');
}

void read_in_coordinates()
{
}
  
void loop() {
  char theta_selection = ' ';
  
  if(Serial.available() > 0)
  {
    char input_character = Serial.read();
    //Serial.print(input_character);
    
    //Serial.write(input_character);
    
    if(input_character == '[')
    {
      while((input_character != 'A') &&
            (input_character != 'B') &&
            (input_character != 'C'))            
      {
        input_character = Serial.read();
        theta_selection = input_character;
      }
      
      while(input_character != ']')
      {
        if(Serial.available() > 0)
        {
          input_character = Serial.read();

          if(input_character != ']')
          {
            input_string.concat(input_character);
          }
          
          //> for continue writing input value
         //Serial.write('>');
          Serial.write(input_character);
        }
      }
      
      delay(1000);
      //int length = input_string.length();

      //Serial.println(length);
      Serial.println(theta_selection);
      
      if(input_string.length() > 0)
      {
          char floatbuf[32];
          input_string.toCharArray(floatbuf, sizeof(floatbuf));
          float input_number = atof(floatbuf);
          Serial.write(theta_selection);
          
          if(theta_selection == 'A')
          {
            theta1 = input_number;
          } 
          else if (theta_selection == 'B')
          {
            theta2 = input_number;
          }
          else if (theta_selection == 'C')
          {
            theta3 = input_number;
          }
          else
          {
            //assign nothing to anything at all
          }
          
          //Serial.print(theta_selection);
          //Serial.print(": ");
          //Serial.println(input_number);
          
          input_string = "";
      }
    }
    
    //X means the input value has been completely read
    Serial.write('X');
  }
  
  if((theta1 >= 0) && (theta2 >= 0) && (theta3 >= 0))
  {    
    //delay(5000);
    if(theta1 < 0) theta1 = 0;
    if(theta2 < 0) theta2 = 0;
    if(theta3 < 0) theta3 = 0;
    if(theta1 > 200) theta1 = 200;
    if(theta2 > 200) theta2 = 200;
    if(theta3 > 200) theta3 = 200;
   
    drive_joints();
  }

  //Serial.write('X');
}

/* drive_joints() simply moves servos 1 and 2 */
void drive_joints() {
  servo1.write(theta1);
  servo2.write(theta2);
  servo3.write(theta3);
    
  theta1 = -1;
  theta2 = -1;  
  theta3 = -1;
  //Serial.print(theta1);  Serial.print(",");   Serial.print(theta2);  Serial.print(",");  Serial.println(theta3);
  //delay(1000);
}
