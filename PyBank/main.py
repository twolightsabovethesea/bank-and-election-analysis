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

csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    for i in csvreader:
        #counts the number of months
        months += 1
        #adds up the total profit/loss
        total = total + int(i[1])
        if previousmonth != None:
            #monthlychange = int(i[1]) - int(previousmonth)
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
#print(f"greatest increase {monthlist[maxdate]} {max(changes)}")
#print(f"greatest decrease {monthlist[mindate]} {min(changes)}")

#print(avechange)
#print(months)
#print(total)

print(f"Financial Analysis\n---------------------------- \nTotal Months: {months}\nTotal: ${total}")
print(f"Average Change: ${round(avechange,2)}")
print(f"Greatest Increase in Profits: {monthlist[maxdate]} (${max(changes)})")
print(f"Greatest Decrease in Profits: {monthlist[mindate]} (${min(changes)})")







