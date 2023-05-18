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
        name1 = []
        name2 = []
        name3 = []
        voter1 = []
        voter2 = []
        voter3 = []

        if candidate_name == (candidate_name -1):
           voter_id = candidate_name
           name1.append(candidate_name)
           voter1.append (candidate_name[1])
           print(name1)
           print(voter1)
           
           candidate_name != (candidate_name -1)
           voter_id = (candidate_name +1) 
           name2.append(candidate_name)
           voter2.append (candidate_name[1])
           print(name2)
           print(voter2)

        else:
            candidate_name = name3
            name3.append(candidate_name)
            voter3.append (candidate_name[1])
            print(name3)
            print(voter3)
           
         # determine the percentage of votes each candidate got  
            candidate_1_percent = (len(voter1) / total_votes) * 100
            candidate_2_percent = (len(voter2) / total_votes) * 100
            candidate_3_percent = (len(voter3) / total_votes) * 100
       
         # determine the total number of votes each candidate got
            total1 = len(list(voter1))
            total2 = len(list(voter2))
            total3 = len(list(voter3))

        # the winner of the election based on popluar vote 
            max = 0
            if total1 > 0:
                max = total1

            if total2 > total1:
                max = total2

            if total3 > total2:
                max = total3
            
            winner - once you have max, correlated that to the name column in that file
            
            printf'Winner: {}'
        