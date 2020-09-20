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
        
    # Create a list to store the variation month by month

    monthly_change = [y-x for x, y in zip(pl_list, pl_list[1:])]

    # Average of the changes in "Profit/Losses" over the entire period

    change_average = round(sum(monthly_change) / len(monthly_change), 2)

    # Greatest Increase in Profits

    # Date when the greatet increase occurred

    date_increase = [x for x, y in zip(date[1:], monthly_change) if y == max(monthly_change)]
    
    # Amount of the greatest increase

    value_increase = [y for x, y in zip(date[1:], monthly_change) if y == max(monthly_change)]

    total_increase = "{} (${})".format(date_increase[0], value_increase[0])
    
    # Greatest Decrease in Profits

    # Date when the greatest decrease occurred

    date_decrease = [x for x, y in zip(date[1:], monthly_change) if y == min(monthly_change)]
    
    # Amount of the greatest decrease 

    value_decrease = [y for x, y in zip(date[1:], monthly_change) if y == min(monthly_change)]
    
    total_decrease = "{} (${})".format(date_decrease[0], value_decrease[0])

    # Print the report
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: {}".format(total_months))
    print("Total: ${}".format(total_pl))
    print("Average Change: ${}".format(change_average))
    print("Greatest increase in Profits: {}".format(total_increase))
    print("Greatest decrease in Profits: {}".format(total_decrease))

# Set variable for results file
results_file = os.path.join("Analysis", "pybank_analysis.txt")

#  Open the results file

with open(results_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write("Total Months: {}\n".format(total_months))
    textfile.write("Total: ${}\n".format(total_pl))
    textfile.write("Average Change: ${}\n".format(change_average))
    textfile.write("Greatest increase in Profits: {}\n".format(total_increase))
    textfile.write("Greatest decrease in Profits: {}\n".format(total_decrease))
