# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)

# note: files are only reading in for me while i have the root folder open in explorer, please keep that in mind if file does not read correctly
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank", "analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
average_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
net_change_list = []
prev = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        #track net change
        if prev != 0:
            net_change_list.append((int(row[1]) - prev))

        # Track the total
        total_months += 1

        # Track the net change
        total_net += int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if (int(row[1]) - prev) > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = (int(row[1]) - prev)

        # Calculate the greatest decrease in losses (month and amount)
        if (int(row[1]) - prev) < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = (int(row[1]) - prev)
        
        #set this profit amount as previous for next iteration
        prev = int(row[1])



# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = []
output.append("Financial Analysis")
output.append("----------------------------")
output.append(f"Total Months: {total_months}")
output.append(f"Total: ${total_net}")
output.append(f"Average Change: ${average_change:.2f}")
output.append(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
output.append(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

#print output summary to terminal
for i in output:
    print(i)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    writer = csv.writer(txt_file)
    
    for i in output:
        writer.writerow([i])
