#Rechnen

#Variablen deklarieren 
Lohnsteuer = 0
Kirchensteuer = 0
Sozialabgaben = 0
Netto = 0
Brutto = 0

#Eingabe
Brutto = float(input("Ihr Bruttolohn: "))

#Rechnung
Lohnsteuer= Brutto * 0.2
Kirchensteuer = Lohnsteuer * 0.09
Sozialabgaben = Brutto * 0.3 * 0.5
Netto = Brutto - Lohnsteuer - Kirchensteuer - Sozialabgaben

#Ausgabe
print("Der Nettolohn ist:",Netto)
