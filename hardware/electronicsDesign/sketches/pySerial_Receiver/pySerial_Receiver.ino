void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  // put your setup code here, to run once:

}
int data;
void loop() {
  // put your main code here, to run repeatedly:
  while(!Serial.available());
  data = Serial.readString().toInt();
  if(data > 240)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else if (data < 240)
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
