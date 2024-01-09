#Creating the OS module
import os

#Importing csv file
import csv

csvpath = os.path.join("..", "Resources", "budget_data")
file = open ('budget_data')
type ("_io.TextIOWrapper")
csvreader = csv.reader(budget_data)
header - []
header = next(csvreader)
header

# with open(csvpath, encoding='UTF-8') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     csv_header = next (csvreader)
# print(f"CSV Header: {csv_header}")




    # for row in csvreader:
    #     print (row )


    # lines = file_handler.read()
    # print(lines)
    # print (type(lines))


    
    # print(csvreader)

    # 

    # 