/*simple LED chaser for beginner..
first see blink example from public example*/

//created by Gundo Victory Tshilimandila
 
//hardware components
// 4 LEDs and 100ohms resisters
//LED pin 12,11,10,9

int led1 = 12;
int led2 = 11;
int led3 = 10;
int led4 = 9;

// the setup routine runs once when you press reset:

void setup() {                
  // initialize the digital pin as an output.
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);  
}


void loop() {
  //change delay for speed you want....
  digitalWrite(led1, HIGH);
  delay(1000);               
  digitalWrite(led1, LOW);    
  delay(1000);       
  digitalWrite(led2, HIGH);
  delay(1000);               
  digitalWrite(led2, LOW);    
  delay(1000);      
  digitalWrite(led3, HIGH);
  delay(1000);               
  digitalWrite(led3, LOW);    
  delay(1000);  
  digitalWrite(led4, HIGH);
  delay(1000);               
  digitalWrite(led4, LOW);    
  delay(1000);        
}
