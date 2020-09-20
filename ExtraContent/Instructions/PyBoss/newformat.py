import os
import csv
import datetime

# Set the path for the file

csv_path = os.path.join("employee_data.csv")

# Open the file

with open(csv_path) as employee_data:
    csv_reader = csv.reader(employee_data, delimiter=",")

    # Read the header row first

    csv_header = next(employee_data)

    # For readability, we will store the colums in variables

    id = []
    name = []
    DOB = []
    SSN = []
    state = []

    # Iterating through the rows to store the values

    for row in csv_reader:
        id.append(row[0])
        name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        state.append(row[4])

    # New format ID
    first_name = [x.partition(" ")[0] for x in name]
    

    last_name = [x.partition(" ")[2] for x in name]
    print(last_name)
    
    # New DOB format

    new_dob = []
    for date in DOB:
        new_dob.append(date[5:7] + "-" + date[8:] + "-" + date[:4]) 
 
    # New SSN
    new_ssn = []
   
    for number in SSN:
        new_ssn.append("***-**" + number[6:])

    # State
    
    abbr_state = []

    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
        
    for name in state:
        abbr_state.append(us_state_abbrev.get(name))

#Zip lists together

cleaned_csv = zip(id, first_name, last_name, new_dob, new_ssn, abbr_state)

# Set the path for the new csv file

new_data_format = os.path.join("new_employee_data.csv")

with open(new_data_format, "w") as csvfile:
    csv_writer = csv.writer(csvfile)

    #Include the header

    csv_writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Write in zipped rows

    csv_writer.writerows(cleaned_csv)

