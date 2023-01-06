import csv
import matplotlib.pyplot as plt

with open('weather_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    spalten = reader.__next__()
    # Finde Spalten-Nr
    index = None
    for i, titel in enumerate(spalten):
        if titel == 'DE_temperature':
            index = i
    print("Die Daten sind in Spalte", index)
    # Extrahiere Daten
    zeit = []
    temp = []
    for row in reader:
        zeit.append(row[0][:4])
        temp.append(float(row[index]))
    print("Die Daten sind extrahiert.")
    # Daten Darstellen
    fig, ax = plt.subplots()
    ax.plot(zeit[::8760], temp[::8760])
    plt.show()
