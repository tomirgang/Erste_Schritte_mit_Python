import csv

with open('cap_warncellids_csv.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        if row[3] == 'Roth':
            print(f'{row[1]}: {row[0]}')
