# import modules
import os
import csv

# set path for .csv file
csv_path = os.path.join('Resources', 'budget_data.csv')

# create counters
months_count = 0
beginning_profit = 0
net_profit = 0
total_changes = 0

# create header lists and profit and loss changes
profit_loss = []
P_L_Changes = []
Dates = []

# Open the CSV and bypass the header
with open(csv_path, newline = '') as csv_file:
    csvreader = csv.reader(csv_file, delimeter = ",")
    csvheader = next(csvreader)

