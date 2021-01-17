import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

vote_count = 0
candidates = {}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        vote_count += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] +=1

print(f'Election Results \n-------------------------\nTotal Votes: {vote_count}\n-------------------------')

khan_prop = candidates['Khan']/vote_count
correy_prop = candidates['Correy']/vote_count
li_prop = candidates['Li']/vote_count
o_tooley_prop = candidates['O\'Tooley']/vote_count

khan_percent = "{:.3%}".format(khan_prop)
correy_percent = "{:.3%}".format(correy_prop)
li_percent = "{:.3%}".format(li_prop)
o_tooley_percent = "{:.3%}".format(o_tooley_prop)

for keys, values in candidates.items():
    print(keys, values)

