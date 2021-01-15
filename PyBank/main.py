# Import requeried libaries
import os 
import csv

# Write down the file path of the csv
csvpath = os.path.join('Resources','budget_data.csv')

month_counter = 0  

with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    print(csvreader)

    header = next(csvreader)

    for row in csvreader:
        month_counter += 1 

print(month_counter)