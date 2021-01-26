int inpin = 7;
int outpin = 8;
int bpin = 6;
int val = 0;
int valb = 0;
int blc = 0;

void setup() {
  // put your setup code here, to run once
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(inpin, INPUT);
  pinMode(outpin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println(val)
  val = digitalRead(inpin);
  valb = digitalRead(bpin);
  if (val == 1) {
    if (blc == 0) {
        delay(1000);
        digitalWrite(LED_BUILTIN, HIGH);
        digitalWrite(outpin, HIGH);
        delay(1000);
        digitalWrite(outpin, LOW);
        digitalWrite(LED_BUILTIN, LOW);
        blc = 1;
      }else {
      
      }
  }else {
    digitalWrite(LED_BUILTIN, LOW);
    blc = 0;
  }
  if (valb == 1) {
    digitalWrite(outpin, HIGH);
  }
}
