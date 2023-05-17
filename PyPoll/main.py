# make the import run on any system and use the csv reading module
import os
import csv

# read the CSV file and convert it
csvpath = os.path.join('C:\\PyPoll\\budget_data.csv')
#textfile = os.path.join('C:\Users\evapa\OneDrive\Desktop\Python\python-challenge\PyPoll\analysis\\election_summary.txt')

#set values for the varaibles in the dataset

# Read the csv and convert it into a list of dictionaries
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row
    header = next(csvreader)
    print(csvfile)
