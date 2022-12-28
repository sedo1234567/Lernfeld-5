#Rechnen
#Widerstands-Parallelschaltung

#Variablen deklarieren 
R1 = int(input("R1: "))
R2 = int(input("R2: "))
Ergebnis = 0

#Rechnung
Ergebnis = (R1 * R2 )/( R1 + R2) 
RoundErgebnis = round(Ergebnis, 4)

#Ausgabe 
print("Das Gesamtwiderstand ist",RoundErgebnis,"Ohm")