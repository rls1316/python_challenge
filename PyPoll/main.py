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
        else: candidate_vote_count[row[2]] = 1

# Loop through candididate_vote_count dictionary to identify each candidates % and determine a winner
for candidate in candidate_vote_count:
    candidate_vote_percentage[candidate] = format((candidate_vote_count[candidate]/total_votes) * 100, '.3f')
    if candidate_vote_count[candidate] > winning_count:
        winning_count = candidate_vote_count[candidate]
        winner = candidate

# Print Results and save to text file
text_file = open('analysis/Election_Results.txt','w')

text_file.write(f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n''')

for candidate, candidate_vote_count in candidate_vote_count.items():
    text_file.write(f'{candidate}: {candidate_vote_percentage[candidate]}% ({candidate_vote_count})\n')

text_file.write(f'''-------------------------
Winner: {winner}
-------------------------''')

text_file.close()

with open('analysis/Election_Results.txt','r') as results:
    Election_Results = results.read()

print(Election_Results)

text_file.close()
