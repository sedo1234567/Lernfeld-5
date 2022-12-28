#Rechnen

#Modul importieren 
import math

#Variablen deklarieren 
X1 = int(input("Runkt x: "))
Y1 = int(input("Punkt y: "))
X2 = int(input("Runkt x: "))
Y2 = int(input("Punkt y: "))
Ergebnis = 0

#Rechnung
Ergebnis =  math.sqrt((X2-X1)**2+(Y2-Y1)**2)

#Ausgabe
print("Der Abstand ist",Ergebnis)