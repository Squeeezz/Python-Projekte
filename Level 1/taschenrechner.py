operator = input("Welchen Operator möchten Sie verwenden (+, -, *, /)?")
zahl1 = float(input("Geben Sie die erste Zahl ein: "))
zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
if operator == "+":
    ergebnis = zahl1 + zahl2
elif operator == "-":
    ergebnis = zahl1 - zahl2
elif operator == "*":
    ergebnis = zahl1 * zahl2
elif operator == "/":
    ergebnis = zahl1 / zahl2

print("Das Ergebnis ist:", ergebnis)