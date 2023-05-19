# make the import run on any system and use the csv reading module
import os
import csv

# read the CSV file and convert it
csvpath = os.path.join('C:\\Users\\evapa\\OneDrive\\Desktop\\Python\\python-challenge\\PyPoll\\Resources\election_data.csv')
textfile = os.path.join('C:\\Users\\evapa\\OneDrive\\Desktop\\Python\\python-challenge\\PyPoll\Analysis\\election_summary.txt')

#set values for the varaibles in the dataset
total_votes = 0
votes ={}
winning_count = 0
winning_candidate = ""

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as vote_file:
  csvreader = csv.reader(vote_file)

  # Read the header row
  header = next(csvreader)

  # set up a loop to read each row and define it
  for row in csvreader:
    voter_id = int(row[0])
    county = str(row[1])
    candidate_name = str(row[2])

    # count the total number of votes
    total_votes += 1
  
    # set up an if statement to collect candidate names and number of votes
    # put those values into a new variable "votes"  
    if candidate_name in votes:
      votes[candidate_name] = votes[candidate_name]+1
    else:
      votes[candidate_name]=0

  print(total_votes)
  print(votes)

  # set up a loop to read each row in the new dictionary "votes"   
  # collect the data to calculate the percentage of votes for each candidate 
  for row in votes:
    cand_votes = votes.get(row)
    cand_percentage = (cand_votes / total_votes)*100
    print(cand_percentage)

    # collect the data to find the winning count and gather the winning name
    if cand_votes > winning_count:
      winning_count = cand_votes
      winning_candidate = row

  print(winning_candidate, winning_count)

    
#write the results to a text file that saves in the Analysis folder    
with open(textfile, 'w') as summary:
  summary.write(f'Election Results\n'
    f'-------------------------\n'
    f'Total Votes: {total_votes}\n'
    f'-------------------------\n'
    f'{votes}: {cand_percentage:.3f}\n'
    f'-------------------------\n'
    f' Winner: {winning_candidate}\n'
    f'-------------------------\n')
      