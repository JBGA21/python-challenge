# Import requeried libaries
import os
import csv

# Write down the file path of the csv
csvpath = os.path.join('Resources', 'budget_data.csv')


month_counter = 0
total_amount = 0
pl_values = []
months = []
changes = []


with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    header = next(csvreader)

    for row in csvreader:
        month_counter += 1
        total_amount += int(row[1])
        pl_values.append(int(row[1]))
        months.append(row[0])


for i in range(len(pl_values)):
    if i == 0:
        continue
    change = pl_values[i] - pl_values[i-1]
    changes.append(change)

average_change = sum(changes) / len(changes)

max_value = max(changes)
max_index = changes.index(max_value)
max_month = months[max_index + 1]

min_value = min(changes)
min_index = changes.index(min_value)
min_month = months[min_index + 1]


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {month_counter}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_month} (${max_value})')
print(f'Lowest Increase in Profits: {min_month} (${min_value})')
