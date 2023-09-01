import csv

with open('randomcsv.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    yr_2000 = dict()

    for row in reader:
        yr_2000[row[0]] = row[2]

    print(yr_2000)

    max_2000 = max(yr_2000.values())

    for k,v in yr_2000.items():
        if max_2000 == v:
            print(f'Busiest month : {k}, Flights : {v.strip()}')
