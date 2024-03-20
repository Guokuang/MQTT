void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while(! Serial) {
    delay(1);
  }
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int cible = random(1,11);
  int essai;


  Serial.print("\n*** Le juste prix ***\n\n");
  for (int i = 1; i<=10;i++) {
    Serial.print("Essai nr");
    Serial.print(i);
    while (Serial.available() == 0) {
      delay(1);
    }
    String str_essai = Serial.readString();
    Serial.print("Saisie : " + str_essai);

    essai = str_essai.toInt();
    if (essai == cible) {
      Serial.print("BRAVO !!!\n");
      break;
    } else if (essai < cible) {
      Serial.print("\nTrop faible\n");
    } else if (essai > cible) {
      Serial.print("\nTrop élevé\n");
    }
    if (i == 10) {
      Serial.print("\nPerdu...\n\n");
      delay(3000);
    }
  }
}
