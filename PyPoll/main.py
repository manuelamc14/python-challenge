# Modules
import os
import csv
import statistics

# Set path for file

csv_path = os.path.join("Resources", "election_data.csv")

# Open csv

with open(csv_path) as csv_file:
    py_poll = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)

    csv_header = next(csv_file)

    # Starting variables

    total_votes = 0
    candidates = []

    for row in py_poll:
        # Total votes

        total_votes += 1
 
        # For readability, we store the data in one variable

        candidates.append(row[2])

    # A complete list of candidates who received votes
    
    candidate_list = list(set(candidates))

