import random

zufallszahl = random.randint(1, 100)
versuche = 0
aktuellerTipp = 0
zahlErraten = False

print("Herzlich Willkommen zum Zahlen-Raten Spiel!")
print("Der Computer generiert eine Zahl zwischen 1 und 100...")

while not (zahlErraten):
    aktuellerTipp = input("Geben sie ihren Tipp ein: ")
    if (int(aktuellerTipp) > zufallszahl):
        print("zu hoch...")
        versuche += 1
    elif (int(aktuellerTipp) < zufallszahl):
        print("zu niedrig...")
        versuche += 1
    else:
        print("richtig")
        versuche += 1
        print("Sie haben", versuche, "gebraucht!")
        zahlErraten = True
