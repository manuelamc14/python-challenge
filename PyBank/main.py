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
   

    for row in csv_reader:
        # total number of months
        total_months += 1
         
        # Add monthly profits or loses

        pl_list.append(int(row[1]))
         
    # net total amount of "Profit/Losses"
    total_pl = sum(pl_list)
    print(total_pl)
    print(total_months) 
    
    # Create a list to store the variance month by month

    variance = [y-x for x, y in zip(pl_list, pl_list[1:])]

    # Average of the changes in "Profit/Losses" over the entire period

    variance_average = round(sum(variance) / len(variance), 2)
    print(variance)
    print(variance_average)

    # Greatest Increase in Profits

 