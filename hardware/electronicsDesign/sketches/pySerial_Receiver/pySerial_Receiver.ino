void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  // put your setup code here, to run once:

}
float data;
void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()>0)
  {
     data = Serial.parseInt();
  }
  if(data > 240.0)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else if (data < 240.0)
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
