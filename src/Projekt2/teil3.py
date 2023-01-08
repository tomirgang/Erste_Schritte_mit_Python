import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as f:
    data = json.load(f)
    # Extrahiere Daten
    jahr = []
    anzahl = []
    for eintrag in data['data']:
        jahr.append(eintrag['Year'])
        anzahl.append(int(eintrag['Population']))
    print("Die Daten sind extrahiert.")
    # Daten Darstellen
    jahr.reverse()
    anzahl.reverse()
    fig, ax = plt.subplots()
    ax.plot(jahr, anzahl)
    plt.show()
