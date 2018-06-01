import os
import csv
import string

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


id = []
firstname = []
lastname = []
dob = []
ssn = []
state = []

csvpath = os.path.join('raw_data\employee_data2.csv')
with open(csvpath, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
   
    # for loop to interate through each row in csv
    for row in csvreader:
        
        # pull Emp ID column and store in new list
        id = id + [row["Emp ID"]]
        
        # reformat Name by splitting into first and last
        split_name = row["Name"].split(" ")
        firstname1 = split_name[0]
        lastname1 = split_name[1]   
        
        # store reformatted name in new list
        firstname = firstname + [firstname1]
        lastname = lastname + [lastname1]
        
        
        # reformat date
        r_dob = row["DOB"].split('-')
        r_dob = f'{r_dob[2]}/{r_dob[1]}/{r_dob[0]}'

        # restore reformatted dob in new list
        dob = dob + [r_dob]
        
        # add ****** to SSN by splitting, reassigning list elements and recombining
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        combined_ssn = "".join(split_ssn)

        # store reformatted dob in new list
        ssn = ssn + [combined_ssn]

        # Use provided dictionary to retrieve state abbreviation
        state_abbrev = us_state_abbrev[row["State"]]

        # store state abbreviation in new list
        state = state + [state_abbrev]


     # zip new/reformatted lists together
r_csv = zip(id, firstname, lastname, dob, ssn, state)

answer_csv = os.path.join('Analysis\Boss_answer.csv')

with open(answer_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile) 
    writer.writerow(["EmpID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(r_csv)

