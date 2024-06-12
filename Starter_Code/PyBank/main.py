import os
import csv

# Get the current working directory
current_dir = os.getcwd()

# Specify the path to the budget_data.csv file relative to the current directory
csvpath = os.path.join(current_dir, "Resources", "budget_data.csv")

print(f"The Path Created: {csvpath}")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

csv_file = "Resources/budet_data.csv"
# Set to store unique months
#unique_months = set()

# Read the CSV file and count unique months
with open(csvpath, "r") as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        # Assuming the date is in the first column (index 0)
        date = row[0]
        month = date.split("-")[0]  # Extract the month part
        month.count(month)

# Calculate the total number of unique months
total_months = len(month)

print(f"Total Number of Months Included in the Dataset: {total_months}")


