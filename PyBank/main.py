# Modules
import os
import csv

# Set path for file

csv_path = os.path.join("..","Resources", "budget_data.csv")

# Open the csv

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)

    csv_header = next(csv_file)

    # The total number of months included in the dataset

    # Starting Variables
     
    total_months = 0
    pl_list = []
    date = []
   

    for row in csv_reader:
        # total number of months
        total_months += 1
         
        # Add monthly profits or loses

        pl_list.append(int(row[1]))
         
        # Add the date

        date.append(str(row[0]))

    # net total amount of "Profit/Losses"
    total_pl = sum(pl_list)

    print(total_pl)
    print(total_months) 
    
    # Create a list to store the variation month by month

    monthly_change = [y-x for x, y in zip(pl_list, pl_list[1:])]
    print(monthly_change[0])

    # Average of the changes in "Profit/Losses" over the entire period

    change_average = round(sum(monthly_change) / len(monthly_change), 2)
    #print(change_average)
    print(change_average)

    # Greatest Increase in Profits

    # date = []
    # for date in csv_reader:
    #     date.append(row[0])
    # print(date)

    date_increase = [x for x, y in zip(date[1:], monthly_change) if y == max(monthly_change)]

    value_increase = [y for x, y in zip(date[1:], monthly_change) if y == max(monthly_change)]

    total_increase = "{} (${})".format(date_increase[0], value_increase[0])
    print(total_increase)

    # Greatest Decrease in Profits
    
    date_decrease = [x for x, y in zip(date[1:], monthly_change) if y == min(monthly_change)]

    value_decrease = [y for x, y in zip(date[1:], monthly_change) if y == min(monthly_change)]
    
    total_decrease = "{} (${})".format(date_decrease[0], value_decrease[0])
    print(total_decrease)