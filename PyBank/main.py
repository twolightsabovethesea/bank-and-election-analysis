import csv
import os
import statistics
#variable for counting the number of months in the file
months = 0
#variable for adding the total amount of profit/loss over period
total = 0
#creates a list of monthly changes in profit/loss
changes = []
#creates an iterable list for using max and min functions
previousmonth = None
changelist = 0
monthlychange = 0
avechange = 0
monthlist = []

#opens the csv file containing the bank data

csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    #reads the data in the csv file
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    for i in csvreader:
        #counts the number of months
        months += 1
        #adds up the total profit/loss
        total = total + int(i[1])
        if previousmonth != None:
            changes.append(int(i[1]) - previousmonth)
            monthlist.append(i[0])
        previousmonth = int(i[1])
avechange = statistics.mean(changes)
maxdate = None
mindate = None
for i in changes:
    if i == max(changes):
        maxdate = changes.index(i)
    if i == min(changes):
        mindate = changes.index(i)

#prints analysis to terminal with appropriate formatting

print(f"Financial Analysis\n---------------------------- \nTotal Months: {months}\nTotal: ${total}")
print(f"Average Change: ${round(avechange,2)}")
print(f"Greatest Increase in Profits: {monthlist[maxdate]} (${max(changes)})")
print(f"Greatest Decrease in Profits: {monthlist[mindate]} (${min(changes)})")

#opens a path to a text file for output
outputpath = os.path.join("analysis","analysis.txt")

#writes results of analysis to a txt file

with open (outputpath, 'w') as file:
    file.write(f"Financial Analysis")
    file.write("\n----------------------------")
    file.write(f"\nTotal Months: {months}")
    file.write(f"\nTotal: ${total}")
    file.write(f"\nAverage Change: ${round(avechange,2)}")
    file.write(f"\nGreatest Increase in Profits: {monthlist[maxdate]} (${max(changes)})")
    file.write(f"\nGreatest Decrease in Profits: {monthlist[mindate]} (${min(changes)})")
