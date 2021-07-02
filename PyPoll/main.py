#imports needed modules
import csv
import os

#sets variables for data to be analyzed
vote_total = 0
candidate_list = []
candidate_dict = {}
Khan = 0
Correy = 0
Li = 0
OTooley = 0
KhanP = 0
CorreyP = 0
LiP = 0
OTooleyP = 0


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
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        #total the votes for each candidate
        if row[2] == "Khan":
            Khan += 1
        elif row[2] == "Correy":
            Correy += 1
        elif row[2] == "Li":
            Li += 1
        elif row[2] == "O'Tooley":
            OTooley += 1

#Calculate percentage of vote for each candidate
KhanP = round((Khan/vote_total)*100, 3)
CorreyP = round((Correy/vote_total)*100, 3)
LiP = round((Li/vote_total)*100, 3)
OTooleyP = round((OTooley/vote_total)*100, 3)

    

#Prints election results to terminal
print(f"Election Results\n---------------------------- \n")
print(f"Total Votes: {vote_total}\n---------------------------- \n")
print(f"Khan: {KhanP}% ({Khan})\n")
print(f"Correy: {CorreyP}% ({Correy})\n")
print(f"Li: {LiP}% ({Li})\n")
print(f"O'Tooley: {OTooleyP}% ({OTooley})\n")
print(f"---------------------------- \n")
print(f"Winner: \n")
print(f"---------------------------- \n")

#writes results to a txt file

outputpath = os.path.join("analysis","analysis.txt")

# with open (outputpath, 'w') as file:
#     file.write(f"Election Results")
#     file.write(f"\n----------------------------")
#     file.write(f"\nTotal Votes: {vote_total}")
#     file.write(f"\n----------------------------")
#     file.write(f"\nKhan: {KhanP}% ({Khan})")
#     file.write(f"\nCorrey: {CorreyP}% ({Correy})")
#     file.write(f"\nLi: {LiP}% ({Li})")
#     file.write(f"\nO'Tooley: {OTooleyP}% ({OTooley})")
#     file.write(f"\n----------------------------")
#     file.write(f"\nWinner: ")
#     file.write(f"\n----------------------------")