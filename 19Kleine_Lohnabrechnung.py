Brutto = float(input("Ihr Bruttolohn: "))

Lohnsteuer= Brutto * 0.2

Kirchensteuer = Lohnsteuer * 0.09

Sozialabgaben = Brutto * 0.3 * 0.5

Netto = Brutto - Lohnsteuer - Kirchensteuer - Sozialabgaben

print("Der Nettolohn ist:",Netto)