# make the import run on any system and use the csv reading module
import os
import csv

# read the CSV file and convert it
csvpath = os.path.join('C:\\Users\\evapa\\OneDrive\\Desktop\\Python\\python-challenge\\PyPoll\\Resources\\election_data.csv')
#textfile = os.path.join('C:\Users\evapa\OneDrive\Desktop\Python\python-challenge\PyPoll\analysis\\election_summary.txt')

#set values for the varaibles in the dataset
total_votes = 0
candidate_list = []

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as vote_file:
    csvreader = csv.reader(vote_file)

    # Read the header row
    header = next(csvreader)

    # set up a loop to read each row and define it
    for row in csvreader:
        voter_id = int(vote_file[0])
        county = str(vote_file[1])
        candidate_name = str(vote_file[2])

        # count the total number of votes
        total_votes = len(list(vote_file))

         # create the list of candidates who received votes
         x = 0
         if x = (row[2]):
            candidate_name == (candidate_name -1)
            candidate_list.append(x)
    
        # determine the percentage of votes each candidate got
        candidate1 = []
        candidate2 = []
        candidate3 = []

        if candidate_name == (candidate_name -1):
            count(candidate_name)
            sum(candidate_name)
            candidate1.append(candidate_name)
            candidate1_votes = 

        if candidate_name != (candidate_name-1):
            candidate_name.append(candidate2)

        elif:
            candidate_name != (candidate_name -1):
           candidate_name.append(candidate3)

        