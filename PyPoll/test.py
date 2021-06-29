import csv
import os
import statistics

months = 0
total = 0
changes = []
iterablelist = []
plvalue = 0
avechange = 0

csvpath = os.path.join('Resources','budget_data.csv') 