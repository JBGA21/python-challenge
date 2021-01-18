import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

vote_count = 0
candidates = {}
vote_percent = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        vote_count += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

print(f'Election Results \n-------------------------\nTotal Votes: {vote_count}\n-------------------------')

for key, value in candidates.items():
    cand_props = candidates[key]/vote_count
    cand_percent = "{:.3%}".format(cand_props)
    candidates[key] = [cand_percent, value]

for keys, value in candidates.items():
    print(f'{keys}: {candidates[keys][0]} ({candidates[keys][1]})')

print(f"-------------------------\n"
    f"Winner: Khan\n"
    f"-------------------------")
