// In this project we will control an LED connected to Arduino pin # 10 via serial communication from python tkinter button.
char serialData;//created a variable name serialData char type
int led1 = 10;// created a variable name led1 int type and assigned as Arduino pin# 10
int led2 = 12;// created a variable name led1 int type and assigned as Arduino pin# 12
void setup()
{
  pinMode (led1, OUTPUT);// initilized led1 as an output
  pinMode (led2, OUTPUT);// initilized led1 as an output
  Serial.begin(9600);// serial comuunucation boud rate-9600
}
void loop()
{
  if (Serial.available() > 0)//check condition-serial data available
    serialData = Serial.read();
  Serial.print(serialData);
  if (serialData == 'a')// if serial data command is 1
  {
    digitalWrite(led1, HIGH);// turn ON the led1
  }
  else if (serialData == 'b')// if serial data is 0
  {
    digitalWrite(led1, LOW);// turn OFF the led1
  }
  if (serialData == 'c')// if serial data command is 1
  {
    digitalWrite(led2, HIGH);// turn ON the led1
  }
  else if (serialData == 'd')// if serial data is 0
  {
    digitalWrite(led2, LOW);// turn OFF the led1
  }
}
