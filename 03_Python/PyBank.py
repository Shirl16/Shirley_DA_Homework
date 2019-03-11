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
    header = next(csvreader)
    
    # count number of months
    for row in csvreader:
      
      data = list(csvreader)
      months = int(len(data))
    
    #------------- the month count is 85 not 86 - need to figure out why--------
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months:") print(months)

#--------------------------------------------------------------------------------------------
# 2. average the profit loss column

