import matplotlib.pyplot as plt

werte = []

for feld_nr in range(0,64):
    anzahl_auf_feld = pow(2, feld_nr)
    werte.append(anzahl_auf_feld)

print("Werte:", werte)

x = range(0,64)
fig, ax = plt.subplots()
ax.plot(x, werte)
plt.show()
