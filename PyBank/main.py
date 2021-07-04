import os
import csv

# save the csv path
csvpath = os.path.join("Resources", "budget_data.csv")

# read the csv and perform the analysis
with open(csvpath) as csvfile:
    # use csv reader to read the csvfile
    csvreader = csv.reader(csvfile, delimiter=',')

    # save the header in order to separate the data you want to use for performing the analysis
    header = next(csvreader)

    # varaibles to save calculations
    total_months = 0
    net_amount = 0
    values = []
    dates = []

    # iterate through the csv
    for row in csvreader:
        total_months += 1
        net_amount += int(row[1])
        values.append(row[1])
        dates.append(row[0])
    # variables to calculate change
    i = 0
    changes = []

    # loop through the profit/loss values
    for x in values:
        if i == 0:
            pass
        else:
            # calculate the change
            change = int(values[i]) - int(values[i-1])
            changes.append(change)

        # update the counter variable
        i += 1

    # calculate the average change
    avg_change = round(sum(changes)/len(changes), 2)

    # calculate the greatest increase in profits
    # get the index of the max change
    max_index = changes.index(max(changes))

    # get the max value in changes
    max_change = max(changes)

    # get the date of the max change
    max_date = dates[24+1]

    # calculate the greatest decrease in profits
    # get the index of the min change
    min_index = changes.index(min(changes))

    # get the min value in changes
    min_change = min(changes)

    # get the date of the min change
    min_date = dates[43+1]


# print the results
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change ${avg_change}")
print(f"Greatest Increase in Profits: {max_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_date} (${min_change})")
