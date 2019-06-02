#The following code was made by arduino

const int buzzer = 9; //buzzer to arduino pin 9
int temperatura = A0;
int val = 0;
void setup()
{
 
  pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
  Serial.begin(9600); 

}

void loop(){
 val = analogRead(temperatura);  // read the input pin
  Serial.println(val);   
    delay(1000);
    
      if(val < 50)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(1500);  
     
  }
  
  else if ( val < 100)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(1000);  
  }

  else if ( val < 120)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(750);  
  }

  else if ( val < 140)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(500);  
  }

   else if ( val < 160)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(300);  
  }

   else if ( val < 180)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(200);  
  }

     else if ( val < 200)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(100);  
  }

   else if ( val > 200)
  {
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);   
    delay(50);  
  }
  
} 