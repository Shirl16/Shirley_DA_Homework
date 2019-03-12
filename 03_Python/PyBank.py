# 1. calc total number of months
#-----------------------------------------------------------------------------------------
# import os and csv
import os
import csv

# path to collect data from csv file
csvpath = os.path.join(".", "budget_data.csv")

# read in the csv file
with open(csvpath) as csvfile:
    
    # split the data in the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # identify header row
   # header = next(csvreader)
    monthList =[]
    
    #identify header row
    header = next(csvreader)

    # count number of months
    for row in csvreader:
     
      monthList.append(str(row[0]))

    print(str(len(monthList)))

     

#--------------------------------------------------------------------------------------------
# 2. average the profit loss column

