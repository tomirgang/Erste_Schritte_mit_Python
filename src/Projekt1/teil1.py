summe = 0

for feld_nr in range(0,64):
    anzahl_auf_feld = pow(2, feld_nr)
    print(f"Anzahl der Weizenkörner auf Feld {feld_nr}:", anzahl_auf_feld)
    summe += anzahl_auf_feld

print("Anzahl der Weizenkörner: ", summe)

# Alternativ

print("Anzahl der Weizenkörner: ", pow(2, 64) - 1)
