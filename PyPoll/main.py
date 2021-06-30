#imports needed modules
import csv
import os

#sets variables for data to be analyzed
vote_total = 0
candidate_list = []

#imports csv containing data for project
csvpath = os.path.join('Resources', 'election_data.csv')

#opens and reads csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    


    