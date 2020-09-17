# Modules
import os
import csv

# Set path for file

csv_path = os.path.join("Resources", "budget_data.csv")

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

    #net total amount of "Profit/Losses"
    total_pl = sum(pl_list)
    
 