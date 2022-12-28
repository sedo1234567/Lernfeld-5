#Aufgabe 3

#Varaiablen deklarieren
Zahl = 0
Rabatt = 0
Ersparnis = 0
Ergebnis = 0

#Eingabe
Zahl = int(input("Umsatz: "))

#Verweigung
if Zahl< 25000:
    Ergebnis = Zahl
    print("Sie erhalten keinen Bonus")
elif Zahl>= 25000 and Zahl<= 50000:
    Rabatt = 2
    Ersparnis = Zahl * 0.02
    Ergebnis = Zahl - Ersparnis
elif Zahl>= 50000 and Zahl<= 75000:
    Rabatt = 3
    Ersparnis = Zahl * 0.03
    Ergebnis = Zahl - Ersparnis
elif Zahl>= 75000 and Zahl<= 100000:
    Rabatt = 4
    Ersparnis = Zahl * 0.04
    Ergebnis = Zahl - Ersparnis
else:
    Rabatt = 5
    Ersparnis = Zahl * 0.05
    Ergebnis = Zahl - Ersparnis

#Ausgabe
print("Sie haben bei uns",Zahl,"Euro Umsatz gemacht und deshalb erhalten Sie einen Bonus von",Rabatt,"%. Sie haben",Ersparnis,
"Euro gespart und deshalb",Ergebnis,"Euro ausgegeben")