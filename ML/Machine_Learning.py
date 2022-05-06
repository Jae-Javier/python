import csv
import numpy as np
import matplotlib as mpl

tempuratures = []

with open('Meteorologydata/' + input("What File?: ") + '.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(', '.join(row))
        tempuratures.append(row[3])

avg_temp = np.average(tempuratures)
print(avg_temp)
