passwort = input("Geben sie ihr Passwort ein: ")
sicherheit = "Sicher"
if len(passwort) < 8:
    sicherheit = "Unsicher"
if not any(char.isupper() for char in passwort):
    sicherheit = "Unsicher"
if not any(char.isdigit() for char in passwort):
    sicherheit = "Unsicher"
print("Ihr Passwort ist:", sicherheit)