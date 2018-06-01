# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# * The total number of months included in the dataset

# * The total amount of revenue gained over the entire period

# * The average change in revenue between months over the entire period

# * The greatest increase in revenue (date and amount) over the entire period

# * The greatest decrease in revenue (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```

# Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Code by Raymond M. Chan 

# Import Dependencies
import pandas as pd
import sys
import csv

# Create reference to CSV file
#csv_path1 = "raw_data/budget_data_1.csv"

text = input("After placing CSV file in the raw_data folder, please input name of file (including .csv for example: budget_data_1.csv):  ")
csvpath = "raw_data/" + text

# Import the CSV into a pandas DataFrame
budgetD1DF = pd.read_csv(csvpath)

# * The total number of months included in the dataset
Months1 = len(budgetD1DF.index)

# * The total amount of revenue gained over the entire period
Total1 = budgetD1DF['Revenue'].sum()

# * The average change in revenue between months over the entire period

budgetD1DF["Next Month's Revenue"] = budgetD1DF["Revenue"].shift(1)
budgetD1DF["Difference Between Revenue"] = budgetD1DF["Revenue"] - budgetD1DF["Next Month's Revenue"]

Average1 = budgetD1DF["Difference Between Revenue"].sum()

TotAverage = Average1/(Months1-1)

MaxInc1 = budgetD1DF["Revenue"].max()
MaxDate1 = budgetD1DF.loc[budgetD1DF["Revenue"] == MaxInc1,"Date"].iloc[0]
MaxDec1 = budgetD1DF["Revenue"].min()
MaxDate2 = budgetD1DF.loc[budgetD1DF["Revenue"] == MaxDec1,"Date"].iloc[0]

# * The greatest increase in revenue (date and amount) over the entire period

print ('```')
print ('Financial Analysis')
print ('----------------------------')
print ('Total Months: ' + str(Months1))
print ('Total Revenue: ' + str(Average1))
print ('Average Revenue Change: '+ str(TotAverage))
print ('Greatest Increase in Revenue: '+ str(MaxDate1) + ' $('+ str(MaxInc1) + ')')
print ('Greatest Decrease in Revenue: '+ str(MaxDate2) + ' $('+ str(MaxDec1) + ')')
print ('```')

#Output to text
sys.stdout = open('output.txt', 'w')
print ('```')
print ('Financial Analysis')
print ('----------------------------')
print ('Total Months: ' + str(Months1))
print ('Total Revenue: ' + str(Average1))
print ('Average Revenue Change: '+ str(TotAverage))
print ('Greatest Increase in Revenue: '+ str(MaxDate1) + ' $('+ str(MaxInc1) + ')')
print ('Greatest Decrease in Revenue: '+ str(MaxDate2) + ' $('+ str(MaxDec1) + ')')
print ('```')
sys.stdout.close()