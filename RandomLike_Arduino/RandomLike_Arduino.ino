#include <Process.h>
#include <LiquidCrystal.h>

#define PinBoton 7

LiquidCrystal LCD(12, 11, 5, 4, 3, 2);

String NombreGlobal = "";
String GanadorGlobal = "";
String IDGlobal = "";

void setup() {
  LCD.begin(16, 2);
  LCD.clear();
  LCD.print("RandomLike ALSW");

  Bridge.begin();        // Iniciar puente entre el Arduino y OpenWRT
  Serial.begin(9600);     // Serial con la computadora

  pinMode(PinBoton, INPUT);
}

void loop() {
  if (digitalRead(PinBoton) == 1) {
    Serial.println("Buscando en FB");
    LCD.setCursor(0, 1);
    LCD.print("Buscando en FB");
    EjecutarFB();
  }
}

void EjecutarFB() {
  ////bin/RandomLike.py
  Process MiScript;
  MiScript.begin("/bin/RandomLike.py");
  MiScript.run();

  String NombreGlobal = "";
  String GanadorGlobal = "";
  String IDGlobal = "";

  while (MiScript.available()) {
    char Carracter = (char)MiScript.read();
    Busca(Carracter, '@', MiScript, &NombreGlobal);
    Busca(Carracter, '#', MiScript, &GanadorGlobal);
    Busca(Carracter, '$', MiScript, &IDGlobal);
  }

  Serial.print("Felicidades al ");
  Serial.print(GanadorGlobal);
  Serial.print(" ");
  Serial.println(NombreGlobal);
  Serial.print("www.fb.com/");;
  Serial.println(IDGlobal);

  LCD.clear();
  LCD.setCursor(0, 0);
  LCD.print(NombreGlobal);
  LCD.setCursor(0, 1);
  LCD.print("fb");
  LCD.setCursor(2, 1);
  LCD.print(IDGlobal);

}

void Busca(char Carracter, char Prueva, Process Script, String *Cadena) {

  if (Carracter == Prueva) {
    while (Script.available()) {
      Carracter = (char)Script.read();
      if (Carracter == '\n') {
        return;
      }
      else {
        *Cadena += Carracter;
      }
    }
  }
}

