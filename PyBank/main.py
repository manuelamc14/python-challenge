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

    # Loop through add the rows
     
    total_months = 0

    for row in csv_file:
        total_months += 1

