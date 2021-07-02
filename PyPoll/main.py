#imports needed modules
import csv
import os

#sets variables for data to be analyzed
vote_total = 0
candidate_list = []
candidate_dict = {}
winnercount = 0
output_dict = {}


#imports csv containing data for project
csvpath = os.path.join('Resources', 'election_data.csv')

#opens and reads csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    for row in csvreader:
        #counts total number of votes
        vote_total += 1
        #creates a list of candidate names
        name = row[2]
        if name not in candidate_list:
            candidate_list.append(name)
            candidate_dict[name] = 0
        candidate_dict[name] = candidate_dict[name] + 1

#finds the percentage of votes for each candidate and the total number of votes for each candidate
for i in candidate_dict:
    tally = candidate_dict.get(i)
    prcnt = round((tally/vote_total) * 100, 3)
    output_dict[i] = [prcnt, tally] 

    if (tally > winnercount):
        winnercount = tally
        winner = i

#Prints analysis to Terminal

print(f"Election Results")
print(f"---------------------------- \n")
print(f"Total Votes: {vote_total}\n")
print(f"---------------------------- \n")
for k,v in output_dict.items():
    print(f"{k}: {v[0]}% ({v[1]})\n")

print(f"---------------------------- \n")
print(f"Winner: {winner}\n")
print(f"---------------------------- \n")


#writes results to a txt file

outputpath = os.path.join("analysis","analysis.txt")

with open (outputpath, 'w') as file:
    file.write(f"Election Results")
    file.write(f"\n----------------------------")
    file.write(f"\nTotal Votes: {vote_total}")
    file.write(f"\n----------------------------")
    for k,v in output_dict.items():
        file.write(f"\n{k}: {v[0]}% ({v[1]})")
    file.write(f"\n----------------------------")
    file.write(f"\nWinner: {winner}")
    file.write(f"\n----------------------------")