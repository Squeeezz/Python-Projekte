zahl1 = input("Gib die erste Zahl ein: ")
zahl2 = input("Gib die zweite Zahl ein: ")
zahl3 = input("Gib die dritte Zahl ein: ")
groesste_zahl = int(zahl1)
if (groesste_zahl < int(zahl2)):
    groesste_zahl = int(zahl2)
if (groesste_zahl < int(zahl3)):
    groesste_zahl = int(zahl3)

print("Die größte Zahl ist:", groesste_zahl)