import csv
import os

load_file = "raw_data/budget_data_1.csv"
output_file = "analysis/budget_analysis_1.txt"

total_months = 0
prev_revenue = 0
revenue_changelist = []
total_revenue = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 1000000000]
 
csvpath = os.path.join(load_file)
with open(csvpath, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
     

# Caluclate total number of months/revenue    
    for row in csvreader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
#print total revenue  

# Calculate greatest increase 
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_changelist = revenue_changelist + [revenue_change]
#print(revenue_changelist) 

# Calculate greatest decrease
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
#print(greatest_increase[1])
#print(greatest_increase[0])

# Calculate greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
#print(greatest_decrease[1])
#print(greatest_decrease[0])

# Calculate the Average Revenue Change
revenue_avg = int(sum(revenue_changelist) / len(revenue_changelist))
#print(revenue_avg)

output = (
    f'\nFinancial Analysis\n'
    f'-----------------------\n'
    f'Total Months: {total_months}\n'
    f'Total Revenue: ${total_revenue}\n'
    f'Average Revenue Change: ${revenue_avg}\n'
    f'Greatest Increase in Revenue: {greatest_increase[0]}: ${greatest_increase[1]}\n'
    f'Greatest Decrease in Revenue: {greatest_decrease[0]}: ${greatest_decrease[1]}\n'

)

print(output)

with open(output_file, 'w') as txt_file:
    txt_file.write(output)