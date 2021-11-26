void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  // put your setup code here, to run once:

}
int xcor,ycor;
void loop() {
  // put your main code here, to run repeatedly:
  while(!Serial.available());
  String s_xcor = Serial.readStringUntil('\n');
  String s_ycor = Serial.readStringUntil('\n');
  xcor = s_xcor.toInt();
  ycor = s_ycor.toInt();
  //data = Serial.readString().toInt();
  if(xcor > 240 && ycor > 240)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else if (xcor < 240 && ycor < 240)
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
