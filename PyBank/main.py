# import modules
import os
import csv

# set path for .csv file
csv_path = os.path.join('Resources', 'budget_data.csv')

# create header lists and profit and loss changes
profit_loss = []
P_L_Changes = []
Dates = []

# Open the CSV and bypass the header
with open(csv_path, newline = '') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    csvheader = next(csvreader)

# Loop through to calculate and append data
    for row in csvreader:
        Dates.append(row[0])
        profit_loss.append(int(row[1]))

    for i in range(len(profit_loss) - 1):
        P_L_Changes.append(profit_loss[i+1] - profit_loss[i])

# gather greatest increase in profits and corresponding date
max_profit = max(P_L_Changes)
max_profit_month = P_L_Changes.index(max_profit) + 1

# gather greatest decrease in losses and corresponding date
min_profit = min(P_L_Changes)
min_profit_month = P_L_Changes.index(min_profit) + 1

# Print Analysis

Financial_Analysis = (f'''Financial Analysis
----------------------------
Total Months: {len(Dates)}
Total: ${sum(profit_loss):.2f}
Average Change: ${sum(P_L_Changes)/len(P_L_Changes):.2f}
Greatest Increase in Profits: {max_profit_month} {max_profit:.2f}
Greatest Decrease in Profits: {min_profit_month} {min_profit:.2f}''')

print(Financial_Analysis)
