# Modules
import os
import csv

# Set path for file

csv_path = os.path.join("..","Resources", "election_data.csv")

# Open csv

with open(csv_path) as csv_file:
    py_poll = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)

    csv_header = next(csv_file)

    # Starting variables

    total_votes = 0

    # Total of number of votes

    for row in py_poll:
        total_votes += 1
    print("Total Votes: {}".format(total_votes))