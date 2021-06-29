import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

