# import modules
import os
import csv

# set path for .csv file
csv_path = os.path.join('Resources', 'election_data.csv')

# create dictionary and variables to hold voting data
total_votes = 0
candidate_vote_count = {}
candidate_vote_percentage = {}
winning_count = 0

# Open the CSV and bypass the header
with open(csv_path, newline = '') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    csvheader = next(csvreader)

# Loop through rows  to calculate and append data
    for row in csvreader:
        total_votes += 1
        if row[2] in candidate_vote_count:
            candidate_vote_count[row[2]] += 1
        else candidate_vote_count[row[2]] = 1

# Loop through candididate_vote_count dictionary to identify each candidates % and determine a winner
    for candidate in candidate_vote_count:
        candidate_vote_percentage[candidate] = format((candidate_vote_count[candidate]/total_votes) * 100, '.3f')
        if candidate_vote_count > winning count:
            winning_count = candidate_vote_count[candidate]
            winner = candidate

# Print Results
Election_Results = (f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidate}: {candidate_vote_percentage[candidate]}% ({candiate_vote_count[candidate]})
-------------------------
Winner: {winner}
-------------------------''')

print(Election_Results)
